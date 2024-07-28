import pytest
from playwright.sync_api import Playwright

from utilities.contstants import BASE_URL


@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
    print(555)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1366, "height": 768})
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    browser.close()

