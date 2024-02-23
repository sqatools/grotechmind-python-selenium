
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..test_data import *
import time


@pytest.mark.parametrize('search_value', ["Selenium", "Python Programming", "Automation"])
def test_search_on_google(browser, search_value):
    browser.get(website_url)
    browser.find_element(By.NAME, "q").send_keys(search_value)
    browser.find_element(By.NAME, "btnK").click()
    time.sleep(3)


# @pytest.mark.parametrize("driver, url", [
#     (webdriver.Chrome(), "https://www.google.co.in"),
#     (webdriver.Firefox(), "https://facebook.com"),
#     (webdriver.Edge(), "https://www.goibibo.com/"),
# ])
# def test_multibrowser_operation(driver, url):
#     driver.get(url)
#     time.sleep(5)
#     driver.close()


# @pytest.mark.parametrize("driver", [webdriver.Chrome(), webdriver.Firefox(), webdriver.Edge()
# ])
# def test_multibrowser_operation_action(driver):
#     driver.get(website_url)
#     driver.find_element(By.NAME, "q").send_keys("Python Programming")
#     driver.find_element(By.NAME, "btnK").click()
#     driver.find_element(By.LINK_TEXT, "Python For Beginners").click()
#     driver.find_element(By.LINK_TEXT, "Downloads").click()
#     driver.find_element(By.LINK_TEXT, "Download Python 3.12.2").click()
#     time.sleep(5)






