from selenium.webdriver.common.by import By

from test_data import  *
import time

def test_goibgo_web(browser):
    browser.get(Goibgo_url)
    browser.find_element(By.XPATH,"//span[@role='presentation']").click()
    browser.find_element(By.XPATH,"//span[text()='Flights']").click()
    browser.find_element(By.XPATH,"//p[text()='One-way']").click()

time.sleep(5)

def test_goibgo_web1(browser):
   browser.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").click()
   browser.find_element(By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']").send_keys("pune")
   browser.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()

   browser.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").click()
   browser.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").send_keys("Mumbai")
   browser.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()

time.sleep(8)
