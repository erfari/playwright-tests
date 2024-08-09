import time

from playwright.sync_api import Playwright, sync_playwright

from utilities.contstants import BASE_URL


# def run(playwright: Playwright):
#     chrome = playwright.chromium
#     browser = chrome.launch()
#     page = browser.new_page()
#     page.goto(BASE_URL)
#     browser.close()
#
#
# if __name__ == '__main__':
#     with sync_playwright() as playwright:
#         run(playwright)

