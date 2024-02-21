import pytest
from selenium import  webdriver
from test import *





@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver