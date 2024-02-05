from Selenium import webdriver
from Selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("python programming")
driver.find_element(By.NAME,"btnK").click()
time.sleep(5)

driver.close()

driver= webdriver.edge()
driver.maximize_window()
driver.implicitly_wait(10)
