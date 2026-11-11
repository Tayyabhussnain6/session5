from __future__ import annotations

from flask import Flask, jsonify, render_template_string, request


ORDER_PAGE = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Create Order</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 42rem; margin: 3rem auto;
           padding: 0 1rem; color: #20242a; }
    form { display: grid; gap: .8rem; max-width: 24rem; }
    label { font-weight: 650; }
    input, button { font: inherit; padding: .55rem; }
    button { background: #225c96; color: white; border: 0; border-radius: .25rem; }
    #message { margin-top: 1.2rem; padding: .8rem; border-left: .3rem solid #225c96; }
    .error { color: #9b1c1c; border-color: #9b1c1c !important; }
  </style>
</head>
<body>
  <main>
    <h1>Create Order</h1>
    <p>Enter integer cents and a discount from 0 to 100 percent.</p>
    <form id="order-form">
      <label for="subtotal">Subtotal in cents</label>
      <input id="subtotal" name="subtotal_cents" type="number" step="1" required>
      <label for="discount">Discount percent</label>
      <input id="discount" name="discount_percent" type="number" step="1" required>
      <button type="submit">Create order</button>
    </form>
    <section id="message" role="status" aria-live="polite" hidden></section>
  </main>
  <script>
    const form = document.querySelector('#order-form');
    const message = document.querySelector('#message');
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      message.hidden = true;
      message.classList.remove('error');
      const payload = {
        subtotal_cents: Number(form.elements.subtotal_cents.value),
        discount_percent: Number(form.elements.discount_percent.value)
      };
      const response = await fetch('/orders', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      });
      const body = await response.json();
      message.hidden = false;
      if (!response.ok) {
        message.classList.add('error');
        message.textContent = `Order rejected: ${body.error.message}`;
        return;
      }
      message.replaceChildren();
      const heading = document.createElement('h2');
      heading.textContent = 'Order confirmed';
      const result = document.createElement('p');
      result.textContent = `Order ${body.id}; total ${body.total_cents} cents`;
      const link = document.createElement('a');
      link.href = `/ui/orders/${body.id}`;
      link.textContent = 'View saved order';
      message.append(heading, result, link);
    });
  </script>
</body>
</html>"""


ORDER_VIEW = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Saved Order</title></head>
<body><main>
  <h1>Saved Order</h1>
  <p>Order {{ order.id }}</p>
  <p>Total {{ order.total_cents }} cents</p>
  <a href="/ui/orders/new">Create another order</a>
</main></body></html>"""


def calculate_total(subtotal_cents: int, discount_percent: int) -> int:
    for name, value in (
        ("subtotal_cents", subtotal_cents),
        ("discount_percent", discount_percent),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if subtotal_cents < 0:
        raise ValueError("subtotal_cents must be at least 0")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    numerator = subtotal_cents * (100 - discount_percent)
    return (numerator + 50) // 100


class InMemoryOrderStore:
    def __init__(self) -> None:
        self._orders: dict[str, dict[str, int | str]] = {}
        self._next_id = 1

    def save(self, order: dict[str, int]) -> dict[str, int | str]:
        order_id = f"ord-{self._next_id}"
        self._next_id += 1
        stored: dict[str, int | str] = {"id": order_id, **order}
        self._orders[order_id] = stored
        return stored.copy()

    def find(self, order_id: str) -> dict[str, int | str] | None:
        order = self._orders.get(order_id)
        return order.copy() if order else None


def create_app(store: InMemoryOrderStore | None = None) -> Flask:
    app = Flask(__name__)
    order_store = store or InMemoryOrderStore()

    def error(code: str, message: str, status: int):
        return jsonify(error={"code": code, "message": message}), status

    @app.get("/ui/orders/new")
    def order_form():
        return render_template_string(ORDER_PAGE)

    @app.get("/ui/orders/<order_id>")
    def order_view(order_id: str):
        stored = order_store.find(order_id)
        if stored is None:
            return "Order does not exist", 404
        return render_template_string(ORDER_VIEW, order=stored)

    @app.post("/orders")
    def create_order():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return error("invalid_json", "Request body must be a JSON object", 400)
        try:
            subtotal = data["subtotal_cents"]
            discount = data["discount_percent"]
            total = calculate_total(subtotal, discount)
        except KeyError as exc:
            return error("missing_field", f"Missing field: {exc.args[0]}", 400)
        except ValueError as exc:
            return error("invalid_value", str(exc), 400)
        stored = order_store.save(
            {"subtotal_cents": subtotal, "discount_percent": discount,
             "total_cents": total}
        )
        return jsonify(stored), 201

    @app.get("/orders/<order_id>")
    def get_order(order_id: str):
        stored = order_store.find(order_id)
        if stored is None:
            return error("not_found", "Order does not exist", 404)
        return jsonify(stored), 200

    return app
