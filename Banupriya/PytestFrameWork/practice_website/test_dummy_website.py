import time
from test_data import *

from selenium.webdriver.common.by import By


def test_dummy_website(browser):
    browser.get(website_url2)
    browser.find_element(By.XPATH, "(//input[@name='firstname'])[1]").send_keys("banu")
    browser.find_element(By.XPATH, "(//input[@name='firstname'])[2]").send_keys("priya")
    browser.find_element(By.ID, "female").click()
    time.sleep(5)