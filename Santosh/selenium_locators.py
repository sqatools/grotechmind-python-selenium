from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
f="Nanded"
F_name="Santosh"
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys(F_name)
driver.find_element(By.ID,"roundtrip").click()
driver.find_element(By.NAME,"fromcity").send_keys(f)
time.sleep(5)

driver.close()
