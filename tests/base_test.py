import re
import time

import allure
import pytest
from playwright.sync_api import Page, expect

from pages.skies_project_author_page import AuthorProject
from pages.skies_projects_page import Projects, ProjectsSearch
from pages.skies_base_page import BasePage
from pages.skies_support_page import Support
from utilities.contstants import EMAIL_TEST_USER, PASSWORD_TEST_USER, BASE_URL, TEST_URL


class TestLogin:

    @pytest.fixture()
    def setup_context(self, page) -> None:
        page.goto(BASE_URL)
        page.set_viewport_size({"width": 2000, "height": 1200})
        yield page

    @pytest.fixture()
    def base_page_init(self, page: Page) -> BasePage:
        return BasePage(page)

    @pytest.fixture()
    def projects_page_init(self, page: Page) -> Projects:
        return Projects(page)

    @pytest.fixture()
    def support_page_init(self, page: Page) -> Support:
        return Support(page)

    @pytest.fixture()
    def author_project(self, page: Page) -> AuthorProject:
        return AuthorProject(page)

    @pytest.fixture()
    def projects_search_page_init(self, page: Page) -> ProjectsSearch:
        return ProjectsSearch(page)

    @pytest.fixture
    @allure.step("Login by credentials")
    def login(self, setup_context, base_page_init: BasePage):
        base_page_init.login(EMAIL_TEST_USER, PASSWORD_TEST_USER)

    @allure.title("Search project")
    def test_search_project(
            self, page: Page, login, base_page_init: BasePage, projects_page_init: Projects,
            projects_search_page_init: ProjectsSearch) -> None:
        with allure.step(f'Ищем проект по поисковому слову в разделе проектов'):
            base_page_init.projects.click()
            projects_page_init.search_by_field(page, 'привет')
            projects_search_page_init.search_project_list.first.wait_for()
        with allure.step(f'Проверяем что нашелся один проект'):
            expect(projects_search_page_init.search_project_list).to_have_count(1)
        with allure.step(f'Переходим на найденный проект и сравниваем что перешли на корректный url'):
            base_page_init.go_to_project('Света Штрейс')
            expect(page).to_have_url(TEST_URL)

    @allure.title("Support project")
    def test_support_project(
            self, page: Page, login, base_page_init: BasePage, author_project: AuthorProject, support_page_init: Support) -> None:
        with allure.step(f'Проверяем что в списке Популярные проекты отображаеся 6 проектов '):
            expect(base_page_init.popular_projects_list).to_have_count(6)
        with allure.step(f'С главной страницы переходим на первый проект в списке Популярные проекты и проверяем'
                         f' наличие вкладок'):
            base_page_init.go_to_first_project()
            expect(author_project.about_author).to_be_visible()
            expect(author_project.author_community).to_be_visible()
            expect(author_project.blog).to_be_visible()
            expect(author_project.support_btn).to_be_visible()
        with allure.step(f'Переходим на вкладку блог и производим операции с комментариями'):
            author_project.go_to_blog()
            author_project.comment_list.last.wait_for()
            with allure.step(f'Оставляем комментарий и проверяем его отображение'):
                author_project.add_comment('тест комент')
                expect(author_project.comment_send_status).to_be_visible()
                page.reload()
                author_project.last_comment_text.wait_for()
                expect(author_project.last_comment_text).to_have_text('тест комент')
        with allure.step(f'Переходим на страницу поддержки кликнув по кнопке'):
            author_project.support_btn.click()
            expect(page).to_have_url(re.compile(r'.*/support'))

    @allure.title("Add to favorite project")
    def test_favorites_project(
            self, page: Page, login, base_page_init: BasePage, author_project: AuthorProject) -> None:
        with allure.step(f'С главной страницы переходим на первый проект в списке Популярные проекты'):
            base_page_init.go_to_first_project()
            project_name = author_project.author_name.text_content()
        with allure.step(f'Добавляем проект в избранное и проверяем что изменился стиль кнопки'):
            author_project.add_to_favorite()
            page.wait_for_timeout(1000)
            expect(author_project.add_favorite_btn).to_have_attribute('src', '/assets/svg/icon-star-blue.svg')
        with allure.step(f'Переходим на страницу избранные проекты и проверяем что проект добавился в избранные, кол-во'
                         f'проектов и название проекта'):
            author_project.move_to_favorites_projects()
            expect(author_project.favorites_projects_list).to_have_count(1)
            expect(author_project.search_favorite_project(page, project_name)).to_have_text('Морячек')
        with allure.step(f'Удаляем проект из избранного'):
            author_project.add_to_favorite()
            page.wait_for_timeout(1000)
            expect(author_project.add_favorite_btn).to_have_attribute('src', '/assets/svg/menu.favoritecreators.svg')

