import pytest
<<<<<<< HEAD
from selenium import webdriver
from test_data import *
=======
from selenium import  webdriver
#from test_data import *
>>>>>>> eea7c9a4f5e372f597728b86421dcf7f87b5c4ca


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
<<<<<<< HEAD
=======

@pytest.fixture(scope="class")
def launch_browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
>>>>>>> eea7c9a4f5e372f597728b86421dcf7f87b5c4ca
