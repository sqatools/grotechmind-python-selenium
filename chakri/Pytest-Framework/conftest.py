import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
