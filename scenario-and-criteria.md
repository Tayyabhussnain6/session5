# Buyer story and acceptance criteria

> As a buyer, I want to submit an order with a discount and read back the confirmed amount, so I can verify what I will be charged.

This is a **local training application**, with one browser form, a Flask API and an in-memory store. It does not represent a production payment or ordering system.

## Agreed rules

- `subtotal_cents` is an integer of at least 0. Boolean values are not valid integers for this contract.
- `discount_percent` is an integer from 0 through 100.
- Calculate the discounted total in integer cents and round to the nearest whole cent, with halves upward. For example, 1,250 cents at 10% gives **1,125 cents**; 106 cents at 10% gives **95 cents**.
- Valid creation saves an order and returns an identifier. A newly created order can be read back with the same identifier and total.
- Invalid input is rejected with readable feedback and does not save an order.

## Observable criteria

| Situation | Required observation |
|---|---|
| A fresh store; buyer submits 1,250 cents and 10% | Confirmation shows **1,125 cents** and a usable order identifier. The first successful order in this fresh store is `ord-1`. |
| Buyer follows **View saved order** | The saved view shows the same identifier and **1,125 cents**. |
| Buyer submits a discount outside 0–100 | The interface shows a readable rejection; no order is saved. A subsequent first valid order in the same fresh store still receives `ord-1`. |

Use the agreed rule to calculate the expected total **before** reading the application's output. A visible confirmation alone is a weak check: it could show the wrong amount or refer to an order that was not saved. The browser test checks the price and follows the public retrieval link.

The prepared test covers the positive create–confirm–retrieve journey. The exploratory activity focuses on invalid input, correction and navigation. Passing these local checks does not establish production behavior, all browsers, accessibility, performance or overall stakeholder acceptance.
