import requests
from config.settings import settings

class ApiClient:
    def __init__(self):
        self.base_url = settings.API_URL
        self.headers = {"X-API-KEY": settings.API_KEY}
        
    def search_movie(self, query: str) -> requests.Response:
        """Поиск фильма по запросу"""
        return requests.get(
            f"{self.base_url}/movie/search",
            params={"query": query},
            headers=self.headers
        )
        
    def search_person(self, name: str) -> requests.Response:
        """Поиск персоны по имени"""
        return requests.get(
            f"{self.base_url}/person/search",
            params={"query": name},
            headers=self.headers
        )
        
    def get_by_id(self, movie_id: str) -> requests.Response:
        """Получение фильма по ID"""
        return requests.get(
            f"{self.base_url}/movie/{movie_id}",
            headers=self.headers
        )