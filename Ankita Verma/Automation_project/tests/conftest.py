import pytest
from selenium import webdriver
from data.session_data import *

@pytest.fixture(scope="class")
def launch_browser(request): #class level browser should work , why request parameter????
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(website_url)
    request.cls.driver = driver # why we are implementing this ??

    yield
    driver.close()
