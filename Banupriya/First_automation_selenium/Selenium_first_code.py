from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.find_element(By.NAME, "q").send_keys("Python Programming")
driver.find_element(By.NAME, "btnK").click()
time.sleep(5)

driver.close()
"""
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#driver.find_element(By.NAME, "q").send_keys("src")
#driver.find_element(By.NAME, "btnK").click()
time.sleep(5)

