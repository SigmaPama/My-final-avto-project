import allure
import pytest
from selenium import webdriver
from utils.ui_helpers import AuthPage, SearchPage, MoviePage
from config.test_data import TestData

@pytest.mark.ui
class TestUIFunctionality:
    
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.auth_page = AuthPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.movie_page = MoviePage(self.driver)
        
    @allure.feature("Авторизация")
    @allure.story("Валидные логин и пароль")
    def test_valid_login_password(self):
        with allure.step("Выполнить авторизацию с логином"):
            self.auth_page.login(TestData.VALID_LOGIN, TestData.VALID_PASSWORD)
        with allure.step("Проверить успешную авторизацию"):
            assert self.auth_page.is_authorized()

    @allure.feature("Авторизация")
    @allure.story("Валидные email и пароль")
    def test_valid_email_password(self):
        with allure.step("Выполнить авторизацию с email"):
            self.auth_page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
        with allure.step("Проверить успешную авторизацию"):
            assert self.auth_page.is_authorized()

    @allure.feature("Поиск")
    @allure.story("Поиск по точному названию существующего фильма")
    def test_search_existing_movie(self):
        with allure.step(f"Выполнить поиск фильма: {TestData.EXISTING_MOVIE}"):
            self.search_page.search_movie(TestData.EXISTING_MOVIE)
        with allure.step("Проверить результаты поиска"):
            assert self.search_page.is_movie_found(TestData.EXISTING_MOVIE)

    @allure.feature("Поиск")
    @allure.story("Поиск по имени режиссера")
    def test_search_director(self):
        with allure.step(f"Выполнить поиск режиссера: {TestData.DIRECTOR_NAME}"):
            self.search_page.search_movie(TestData.DIRECTOR_NAME)
        with allure.step("Проверить наличие режиссера в результатах"):
            assert self.search_page.is_director_found(TestData.DIRECTOR_NAME)

    @allure.feature("Оценка")
    @allure.story("Постановка оценки фильму авторизованным пользователем")
    def test_set_movie_rating(self):
        with allure.step("Предварительная авторизация пользователя"):
            self.auth_page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
        with allure.step(f"Выполнить поиск фильма: {TestData.MOVIE_TO_RATE}"):
            self.search_page.search_movie(TestData.MOVIE_TO_RATE)
        with allure.step("Открыть страницу фильма и поставить оценку"):
            self.movie_page.set_rating(8)
        with allure.step("Проверить, что оценка установлена"):
            assert self.movie_page.is_rating_set()