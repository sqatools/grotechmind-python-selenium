from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]").send_keys("Shekhar")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]").send_keys("Tyagi")
time.sleep(1)
driver.find_element(By.ID, "male").click()
time.sleep(1)
driver.find_element(By.ID,"oneway").click()
time.sleep(1)
driver.find_element(By.ID,"birthday").click()
time.sleep(2)
