import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.goibibo.com")
    return driver
