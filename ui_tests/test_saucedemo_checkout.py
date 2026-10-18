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
    expect(page.get_by_role("heading", name="Checkout: Complete!")).to_be_visible()


@pytest.mark.ui
def test_invalid_login_shows_feedback(page: Page):
    login(page, "invalid_user", "wrong_password")
    expect(page.locator("[data-test='error']")).to_contain_text("Username and password do not match")
    expect(page).to_have_url(BASE_URL + "/")


@pytest.mark.ui
@pytest.mark.parametrize(
    ("missing_field", "error_message"),
    [
        ("First Name", "First Name is required"),
        ("Last Name", "Last Name is required"),
        ("Zip/Postal Code", "Postal Code is required"),
    ],
)
def test_checkout_requires_all_customer_fields(page: Page, missing_field: str, error_message: str):
    login(page)
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    page.get_by_role("button", name="Checkout").click()
    values = {"First Name": "QA", "Last Name": "Portfolio", "Zip/Postal Code": "12345"}
    for field, value in values.items():
        if field != missing_field:
            page.get_by_placeholder(field).fill(value)
    page.get_by_role("button", name="Continue").click()
    expect(page.locator("[data-test='error']")).to_contain_text(error_message)
    expect(page).to_have_url(BASE_URL + "/checkout-step-one.html")


@pytest.mark.ui
def test_cart_can_be_edited_before_checkout(page: Page):
    login(page)
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(1)
    page.get_by_role("button", name="Remove").click()
    expect(page.locator(".cart_item")).to_have_count(0)
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
