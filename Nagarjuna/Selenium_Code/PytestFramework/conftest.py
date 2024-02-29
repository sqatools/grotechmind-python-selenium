import pytest
from selenium import webdriver
from test_data import *

@pytest.fixture(scope="function")
def initial_setup():
    print("\n Testing begins")
    yeild
    print("\n Testing ends")


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
