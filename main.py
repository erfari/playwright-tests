import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright):
    chrome = playwright.chromium
    browser = chrome.launch()
    page = browser.new_page()
    page.goto("https://stage.skies.land/")
    time.sleep(5)
    browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)

