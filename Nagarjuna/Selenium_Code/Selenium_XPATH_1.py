from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@value='radio_123'])").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@id='firstname'][1])").send_keys("naga")
time.sleep(1)
driver.find_element(By.XPATH,"(//input[@id='firstname'][2])").send_keys("arjun")
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@type='date'][1])").send_keys("21/07/1993")
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@id='male'])").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//select[@id='admorepass'])").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@id='oneway'])").click()
time.sleep(1)




driver.close()
