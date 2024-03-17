import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_data import *

options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", prefs)

@pytest.fixture(scope="function")
def initial_setup():
    print("\n Test begins")
    yield
    print("\n End of the tests")


@pytest.fixture(scope="session")
def browser():

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
