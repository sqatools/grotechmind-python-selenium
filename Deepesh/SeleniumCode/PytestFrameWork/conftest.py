import pytest
from selenium import  webdriver
#from test_data import *


@pytest.fixture(scope="function")
def initial_setup():
    print("\n Test begins")
    yield
    print("\n End of the test")


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope="class")
def launch_browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()