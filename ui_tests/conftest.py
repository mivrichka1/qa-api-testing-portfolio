import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):
    os.makedirs("artifacts", exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page
        if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
            context.tracing.stop(path=f"artifacts/{request.node.name}-trace.zip")
            page.screenshot(path=f"artifacts/{request.node.name}-failure.png", full_page=True)
        else:
            context.tracing.stop()
        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())
