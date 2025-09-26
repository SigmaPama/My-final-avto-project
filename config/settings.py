import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = "https://www.kinopoisk.ru"
    API_URL = "https://api.kinopoisk.dev/v1.4"
    API_KEY = os.getenv("API_KEY")
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"  

settings = Settings()