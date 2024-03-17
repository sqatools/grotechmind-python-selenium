from selenium import  webdriver
from Data.Session_Data import *
import pytest





@pytest.fixture(scope='class')

def launch_browser(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(9)
    request.cls.driver=driver
    yield
    driver.close()

