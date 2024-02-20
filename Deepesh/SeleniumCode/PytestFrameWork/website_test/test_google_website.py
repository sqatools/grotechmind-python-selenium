import time

import pytest
from selenium.webdriver.common.by import By
from ..test_data import *

def test_search_on_google(browser):
    browser.get(website_url)
    browser.find_element(By.NAME, "q").send_keys("Python Programming")
    browser.find_element(By.NAME, "btnK").click()

def test_python_website(browser):
    browser.find_element(By.LINK_TEXT, "Python For Beginners").click()
    browser.find_element(By.LINK_TEXT, "Downloads").click()
    browser.find_element(By.LINK_TEXT, "Download Python 3.12.2").click()
    time.sleep(5)





