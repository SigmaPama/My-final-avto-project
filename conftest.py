import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.settings import settings

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.BROWSER)

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = Options()
        if settings.HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    driver.get(settings.BASE_URL)
    
    yield driver
    driver.quit()