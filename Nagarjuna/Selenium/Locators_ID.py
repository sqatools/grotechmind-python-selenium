from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.ID,"admorepass").click()
driver.find_element(By.ID,"fromcity").send_keys("hyderabad")
driver.find_element(By.ID,"destcity").send_keys("Bangalore")
driver.find_element(By.ID,"departdate").click()
driver.find_element(By.ID,"oneway").click()
driver.find_element(By.ID,"eamil").click()
driver.find_element(By.ID,"billing_name").send_keys("nagarjuna")
driver.find_element(By.ID,"billing_phone").send_keys("934454363532")
driver.find_element(By.ID,"billing_email").send_keys("naga@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys("bangalore")
driver.find_element(By.ID,"billing_country").click()
