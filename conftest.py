import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    # Time-out for page load
    page.set_default_timeout(10000)

    yield page

    print("-------------- TC is finished ------------------")

    # Close session
    page.close()
