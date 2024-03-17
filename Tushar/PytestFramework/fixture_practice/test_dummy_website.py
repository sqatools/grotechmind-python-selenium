from selenium.webdriver.common.by import By
import time
from test_data import *

def test_dummy_website(browser):
    browser.get(dummy_url1)
    browser.find_element(By.XPATH,"//a[text()='Online Training']").click()
    browser.find_element(By.XPATH,"//parent::li//following-sibling::a[text()='Manual Testing']//following::a[text()='Manual Testing']").click()

time.sleep(5)

# python -m pytest -v  -s .\fixture_practice\

def test_dummy_website_data(browser):
    browser.get(dummy_url1)
    browser.find_element(By.XPATH,"(//input[@value='checkbox'])[1]").click()

    time.sleep(5)
