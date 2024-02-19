from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com")
time.sleep(1)
driver.find_element(By.XPATH,"//span[@role='presentation']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p[text()='Enter city or airport']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[text()='New Delhi, India']//ancestor::li").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input").send_keys("Delhi")
time.sleep(1)
driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input").send_keys("Bangalore")
time.sleep(1)
driver.find_element(By.XPATH,"//p[text()='4']//parent::div[contains(@aria-label,'Feb')]").click()
driver.find_element(By.XPATH,"//")

driver.close()
