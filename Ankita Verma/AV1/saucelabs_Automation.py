from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(1)
#driver.find_element(By.XPATH,"//a[@id='inventory_sidebar_link']").click()
driver.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']").click()
time.sleep(3)
element = driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]")
assert element
