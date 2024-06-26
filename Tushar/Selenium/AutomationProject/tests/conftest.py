import pytest
from selenium import webdriver
from data.session_data import *

@pytest.fixture(scope='class')
def launch_browser(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    #driver.get(website_url_3)
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()

@pytest.fixture(scope='class')
def launch_browser_dummy(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(website_url_3)
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()
