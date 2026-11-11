import pytest
from playwright.sync_api import Page, expect


def test_create_confirm_and_retrieve(page: Page, app_url: str):
    page.goto(f"{app_url}/ui/orders/new")
    page.get_by_label("Subtotal in cents").fill("1250")
    page.get_by_label("Discount percent").fill("10")
    page.get_by_role("button", name="Create order").click()

    expect(page.get_by_text("Order ord-1; total 1125 cents")).to_be_visible()
    page.get_by_role("link", name="View saved order").click()

    pytest.fail("TODO: assert the saved-order heading and exact retrieved total")
