import time

import allure
import pytest
from playwright.sync_api import Page

from pages.skies_base_page import LoginPage, BasePage
from utilities.contstants import EMAIL_TEST_USER, PASSWORD_TEST_USER


class TestLogin:
    @pytest.fixture
    def setup(self, new_page):
        self.page = new_page
        self.base_page = BasePage(self.page)
        self.login_page = LoginPage(self.page)


    @allure.title("Get base page")
    def test_valid_login1(self, setup):
        self.base_page.go_to_login()
        self.login_page.login(EMAIL_TEST_USER, PASSWORD_TEST_USER)
        time.sleep(5)

