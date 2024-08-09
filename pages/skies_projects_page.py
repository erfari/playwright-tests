import time
from dataclasses import dataclass

from allure_commons._allure import step
from playwright.sync_api import Page

import allure


@allure.description("Projects page")
@dataclass
class Projects:
    def __init__(self, page: Page):
        self.page = page
        self.search_field = page.locator("//input[@type='search']")

    @step('Поиск проекта по слову привет')
    def search_by_field(self, page: Page, text):
        self.search_field.fill(text)
        page.keyboard.press('Enter')

    def go_to_category(self, page: Page, category):
        (page.locator("//div[@class='creators-categories__category-list']/div[contains(text(), '{}')]".format(category))
         .click())


@allure.description("Result project search page")
@dataclass
class ProjectsSearch:
    def __init__(self, page: Page):
        self.page = page
        self.search_project_list = page.locator("//div[@class='creator-badge-list__container']/creator-badge")
