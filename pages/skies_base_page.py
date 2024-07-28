import time
from dataclasses import dataclass
from playwright.sync_api import Page

import allure


@allure.description("Base page")
@dataclass
class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.feed_field = page.get_by_text(" Лента ")
        self.projects_field = page.get_by_text(" Проекты ")
        self.registration_field = page.get_by_text(" Регистрация ")
        self.login_field = page.get_by_text("Войти")

    def go_to_login(self):
        self.login_field.click()


@allure.description("Base page")
@dataclass
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.locator("//input[@name='email']")
        self.password = page.locator("//input[@name='password']")
        self.login_btn = page.locator("//input[@type='submit']")
        self.password_foreign_btn = page.get_by_text("Забыли пароль?")

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.login_btn.click()
        time.sleep(5)

