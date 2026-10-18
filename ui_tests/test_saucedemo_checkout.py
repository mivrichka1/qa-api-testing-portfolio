import os

import pytest
from playwright.sync_api import Page, expect

BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com").rstrip("/")


def login(page: Page, username: str = "standard_user", password: str = "secret_sauce"):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


@pytest.mark.ui
def test_standard_user_can_complete_checkout(page: Page):
    login(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("First Name").fill("QA")
    page.get_by_placeholder("Last Name").fill("Portfolio")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")
    page.get_by_role("button", name="Continue").click()
    expect(page.get_by_text("Payment Information")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.locator(".summary_subtotal_label")).to_contain_text("29.99")
    expect(page.locator(".summary_total_label")).to_contain_text("32.39")
    page.get_by_role("button", name="Finish").click()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    expect(page.get_by_text("Your order has been dispatched")).to_be_visible()


@pytest.mark.ui
def test_invalid_login_shows_error(page: Page):
    login(page, username="invalid_user")
    expect(page.get_by_text("Username and password do not match")).to_be_visible()


@pytest.mark.ui
@pytest.mark.parametrize(
    ("first_name", "last_name", "postal_code", "expected_error"),
    [("", "Portfolio", "12345", "First Name is required"),
     ("QA", "", "12345", "Last Name is required"),
     ("QA", "Portfolio", "", "Postal Code is required")],
)
def test_checkout_requires_customer_fields(page: Page, first_name, last_name, postal_code, expected_error):
    login(page)
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("First Name").fill(first_name)
    page.get_by_placeholder("Last Name").fill(last_name)
    page.get_by_placeholder("Zip/Postal Code").fill(postal_code)
    page.get_by_role("button", name="Continue").click()
    expect(page.get_by_text(expected_error)).to_be_visible()


@pytest.mark.ui
def test_cart_can_be_edited_before_checkout(page: Page):
    login(page)
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(1)
    page.get_by_role("button", name="Remove").click()
    expect(page.locator(".cart_item")).to_have_count(0)
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
