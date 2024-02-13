from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.goibibo.com/")
driver.find_element(By.XPATH,"//span[@role='presentation']").click()
driver.find_element(By.XPATH,"//span[text()='Flights']").click()
driver.find_element(By.XPATH,"//p[text()='One-way']").click()
# driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").click()
# driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']").send_keys("pune")



driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").click()
driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']").send_keys("pune")
driver.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()

driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").click()
driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").send_keys("Mumbai")
driver.find_element(By.XPATH,"//span[@class='autoCompleteTitle ']").click()

