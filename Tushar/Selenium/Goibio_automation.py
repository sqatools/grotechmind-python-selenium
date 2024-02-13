from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.goibibo.com/")

# 1 Verify that users can successfully register for a new account.
# 2 Validate the login functionality with valid credentials.
# 3Test login with invalid credentials and ensure proper error messages are displayed.

#driver.find_element(By.XPATH,"//p[text()='LOGIN / SIGNUP'][1]").click()
driver.find_element(By.XPATH,"//input[@name='phone']").send_keys('9860560531')







"""
driver.find_element(By.XPATH,"//span[@role='presentation']").click()
driver.find_element(By.XPATH,"//span[text()='Flights']").click()
driver.find_element(By.XPATH,"//p[text()='One-way']").click()

#driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").click()
#driver.find_element(By.XPATH,"//input[@type='text']").send_keys("nashik")

# driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").click()
# driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']").send_keys("pune")
# driver.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()
#
# driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::p").click()
# #driver.find_element(By.XPATH,"//input[@type='text']").send_keys("mumbai")
# driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").send_keys("Mumbai")
# driver.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()


driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").click()
driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']").send_keys("pune")
driver.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()

driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").click()
driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").send_keys("Mumbai")
driver.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()
driver.find_element(By.XPATH,"//p[text()='14']//parent::div[contains(@aria-label,'Feb')]").click()

#driver.find_element(By.XPATH,"//span[text()='Departure']//following::span[@class='sc-12foipm-22 cUvQPq fswDownArrow']").click


"""

time.sleep(5)
driver.close()
