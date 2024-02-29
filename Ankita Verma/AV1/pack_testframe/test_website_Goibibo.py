from selenium.webdriver.common.by import By
import time
from data_file import *
def test_start(browser):
    browser.get(url)
    browser.find_element(By.XPATH,"//span[@role='presentation']").click()
    time.sleep(1)
    browser.find_element(By.XPATH,"//span[text()='From']//following-sibling::p[text()='Enter city or airport']").click()
    time.sleep(1)
    browser.find_element(By.XPATH,"//span[text()='New Delhi, India']//ancestor::li").click()
    time.sleep(1)
    browser.find_element(By.XPATH,"//span[text()='From']//following-sibling::input").send_keys("Delhi")
    time.sleep(1)
    browser.find_element(By.XPATH,"//span[text()='To']//following-sibling::input").send_keys("Bangalore")
    time.sleep(1)
    browser.find_element(By.XPATH,"//p[text()='4']//parent::div[contains(@aria-label,'Feb')]").click()

