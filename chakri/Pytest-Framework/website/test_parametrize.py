import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from test_data import *

'''
@pytest.mark.parametrize("search",["chakri insights","telugu badi","kranthi vlogger","journalist sai"])
def test_youtube(website,search):
    website.get(google)
    website.find_element(By.NAME,"q").send_keys(search)
    website.find_element(By.NAME,"btnK").click()
    time.sleep(5)



@pytest.mark.parametrize("driver,url", [
    (webdriver.Chrome(), "https://www.facebook.com/"),
    (webdriver.Firefox(), "https://www.youtube.com/"),
    (webdriver.Edge(), "https://www.instagram.com/")
])
def test_multi_browser(driver, url):
    driver.get(url)
    time.sleep(5)
    driver.close()
'''
@pytest.mark.parametrize("driver",[webdriver.Chrome()])
def test_multi_browser_same_value(driver):
    driver.get(google)
    driver.find_element(By.NAME,"q").send_keys("Python programming")
    driver.find_element(By.NAME,"btnK").click()
    time.sleep(5)
    driver.close()

