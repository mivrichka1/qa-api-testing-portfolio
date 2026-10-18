import os

import pytest
from playwright.sync_api import expect, sync_playwright

BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com").rstrip("/")

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.mark.ui
def test_user_can_complete_checkout(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()

    page.get_by_placeholder("First Name").fill("QA")
    page.get_by_placeholder("Last Name").fill("Portfolio")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")
    page.get_by_role("button", name="Continue").click()
    expect(page.get_by_text("Payment Information")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    page.get_by_role("button", name="Finish").click()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
