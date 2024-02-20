from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

driver.find_element(By.XPATH,"//a[contains(text(),'Software Testing Methods ')]").click()
time.sleep(3)

browser_windows = driver.window_handles
print("Total number of windows :", browser_windows)
driver.switch_to.window(browser_windows[1])

driver.find_element(By.ID,"ContactForm2_contact-form-name").send_keys("nagarjuna")
driver.find_element(By.CLASS_NAME,"contact-form-email").send_keys("nagadaf@gmail.com")
driver.find_element(By.XPATH,"//input[@type='button'][1]").click()
time.sleep(6)

driver.close()

driver.switch_to.window(browser_windows[0])
time.sleep(5)
driver.find_element(By.XPATH,"//li//a[contains(text(),'Home')]").click()
time.sleep(5)
driver.close()
