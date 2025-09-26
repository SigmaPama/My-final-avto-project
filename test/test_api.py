import allure
import pytest
from utils.api_client import ApiClient
from config.test_data import TestData

@pytest.mark.api
class TestAPIFunctionality:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = ApiClient()
        
    @allure.feature("API Поиск")
    @allure.story("Поиск по названию фильма на кириллице")
    def test_search_cyrillic_movie(self):
        response = self.api_client.search_movie(TestData.CYRILLIC_MOVIE)
        assert response.status_code == 200
        assert TestData.CYRILLIC_MOVIE in response.json()["names"]
        
    @allure.feature("API Поиск")
    @allure.story("Поиск по названию фильма на латыни")
    def test_search_latin_movie(self):
        response = self.api_client.search_movie(TestData.LATIN_MOVIE)
        assert response.status_code == 200
        assert TestData.LATIN_MOVIE in response.json()["names"]
        
    @allure.feature("API Поиск")
    @allure.story("Поиск актера по имени на кириллице")
    def test_search_cyrillic_actor(self):
        response = self.api_client.search_person(TestData.ACTOR_NAME)
        assert response.status_code == 200
        assert any(TestData.ACTOR_NAME in person["name"] for person in response.json()["docs"])
        
    @allure.feature("API Поиск")
    @allure.story("Поиск по некорректному ID")
    def test_search_invalid_id(self):
        response = self.api_client.get_by_id(TestData.INVALID_ID)
        assert response.status_code == 404
        
    @allure.feature("API Поиск")
    @allure.story("Поиск с пустым полем запроса")
    def test_search_empty_query(self):
        response = self.api_client.search_movie("")
        assert response.status_code == 400