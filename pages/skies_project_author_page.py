import time
from dataclasses import dataclass

from allure_commons._allure import step
from playwright.sync_api import Page, Locator

import allure
from pytest_playwright.pytest_playwright import context


@allure.description("Projects page")
@dataclass
class AuthorProject:
    def __init__(self, page: Page):
        self.page = page
        self.about_author = page.locator("//div[contains(text(), 'Об авторе')]")
        self.author_name = page.locator("//h1")
        self.blog = page.locator("//div[contains(text(), 'Блог')]")
        self.author_community = page.locator("//div[contains(text(), 'Сообщество')]")
        self.comment_btn = page.locator("//*[@class='container']/post[1]//button[@type='submit']")
        self.support_btn = page.locator("//a[contains(text(), 'Поддерживать')]")
        self.comment_textarea = page.locator("//*[@class='container']/post[1]//textarea")  #first project
        self.comment_list = page.locator(
            "//post[position()=1]//div[@class='comment-list__comments-list']/comment")  #first project
        self.last_comment_text = page.locator("//post[position()=1]//div["
                                              "@class='comment-list__comments-list']/comment[5]//p")  #first project
        # last comment
        self.comment_send_status = page.locator("//*[contains(span, 'Комментарий отправлен')]")

        # тут нужно добавить якорей к кнопке, чтобы можно было легче искать
        self.add_favorite_btn = page.locator("//button/img")
        self.favorites_projects_btn = page.locator("//span[contains(text(), 'Избранные проекты')]")
        self.favorites_projects_list = page.locator("//*[@class='creators__content']/div")

    @step('Перейти на вкладку блога')
    def go_to_blog(self):
        self.blog.click()

    @step('Оставить комментарий')
    def add_comment(self, comment):
        self.comment_textarea.fill(comment)
        self.comment_btn.click()

    @step('Добавление проекта в избранное')
    def add_to_favorite(self):
        self.add_favorite_btn.click()

    @step('Переход на вкладку Избранные проекты на странице автора')
    def move_to_favorites_projects(self):
        self.favorites_projects_btn.click()

    @step('Поиск в списке избранных проектов')
    def search_favorite_project(self, page: Page, author_name) -> Locator:
        return page.locator("//*[@class='creators__content']//span[contains(text(), '{}')]".format(author_name))
