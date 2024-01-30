from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("python Programming")
driver.find_element(By.NAME,'btnK').click()

time.sleep(5)
driver.close()
"""

###########################

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.ID,'male').click()
driver.find_element(By.ID,'female').click()
driver.find_element(By.ID,'billing_name').send_keys("travel.com")
driver.find_element(By.ID,'billing_phone').send_keys("9860560531")
driver.find_element(By.ID,'billing_email').send_keys("tushar@gmail.com")
driver.find_element(By.ID,'billing_address').send_keys('Pune')
time.sleep(10)
driver.close()
