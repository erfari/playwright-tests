from allure_commons._allure import step
from playwright.sync_api import Browser, Playwright, Page

import allure


@allure.description("Base page")
class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.auth = page.locator("//*[contains(a, 'Войти')]")
        self.projects = page.locator("//*[contains(a, 'Проекты')]")
        self.popular_projects_list = page.locator("//div[@class='creator-badge-list__container']/creator-badge")
        self.first_project = page.locator("//*[@class='creator-badge-list__container']/creator-badge[1]//img")
        self.email = page.locator("//input[@name='email']")
        self.password = page.locator("//input[@name='password']")
        self.login_btn = page.locator("//input[@type='submit']")
        self.password_foreign_btn = page.get_by_text("Забыли пароль?")

    @step('Авторизация пользователя')
    def login(self, email: str, password: str) -> None:
        self.auth.click()
        self.email.fill(email)
        self.password.fill(password)
        self.login_btn.click()

    @step('Переход на страницу проекта')
    def go_to_project(self, project_name):
        self.popular_projects_list.first.wait_for()
        self.popular_projects_list.first.get_by_text(project_name).click()

    @step('Переход на страницу первого проекта')
    def go_to_first_project(self):
        self.popular_projects_list.first.wait_for()
        self.first_project.click()
