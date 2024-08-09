import time
from dataclasses import dataclass

from allure_commons._allure import step
from playwright.sync_api import Page

import allure
from pytest_playwright.pytest_playwright import context


@allure.description("Projects page")
@dataclass
class Support:
    def __init__(self, page: Page):
        self.page = page
        self.action_support_btn = page.locator("//button[contains(text(), 'Поддерживать')]")

    @step('Нажатие накнопку поддержки автора')
    def support_author(self):
        self.action_support_btn.click()
