from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15, poll_frequency=2) # explicit wait

driver.get("https://www.facebook.com/")

element = driver.find_element(By.ID, "email")
print("attrib_value :", element.get_attribute('placeholder'))
print("attrib value 2 :",element.get_attribute("data-testid"))

driver.close()