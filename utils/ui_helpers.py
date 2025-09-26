from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    """Класс для работы со страницей авторизации"""
    
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username: str, password: str):
        """Выполнить авторизацию"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='login-button']"))
        ).click()
        
        self.driver.find_element(By.NAME, "login").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        
    def is_authorized(self) -> bool:
        """Проверить, что авторизация прошла успешно"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test-id='user-avatar']"))
        ).is_displayed()

class SearchPage:
    """Класс для работы со страницей поиска"""
    
    def __init__(self, driver):
        self.driver = driver
        
    def search_movie(self, query: str):
        """Выполнить поиск по запросу"""
        search_field = self.driver.find_element(By.NAME, "kp_query")
        search_field.clear()
        search_field.send_keys(query)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        
    def is_movie_found(self, title: str) -> bool:
        """Проверить, что фильм найден"""
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".search_results"), title)
        )
        
    def is_director_found(self, name: str) -> bool:
        """Проверить, что режиссер найден"""
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".search_results"), name)
        )

class MoviePage:
    """Класс для работы со страницей фильма"""
    
    def __init__(self, driver):
        self.driver = driver
        
    def set_rating(self, rating: int):
        """Установить оценку фильму"""
        self.driver.find_element(By.CSS_SELECTOR, f"[data-rate='{rating}']").click()
        
    def is_rating_set(self) -> bool:
        """Проверить, что оценка установлена"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".rating-set"))
        ).is_displayed()