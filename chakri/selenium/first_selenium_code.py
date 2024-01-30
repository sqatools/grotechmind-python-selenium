from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
'''driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.find_element(By.NAME,"q").send_keys("python programming")
driver.find_element(By.NAME, "btnK").click()
time.sleep(5)

driver.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(15)
driver.find_element(By.NAME,"email").send_keys("9154660350")
driver.find_element(By.NAME,"pass").send_keys("Chakri@180")
driver.find_element(By.NAME,"login").click()
'''

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.NAME,"firstname").send_keys("Chakri")
driver.find_element(By.ID,"birthday").send_keys("21/02/1998")
driver.find_element(By.ID,"male").click()
driver.find_element(By.NAME,"fromcity").send_keys("hyderabad")
driver.find_element(By.NAME,"destcity").send_keys("rajahmundary")
driver.find_element(By.ID,"departdate").send_keys("30/01/2024")
driver.find_element(By.ID,"returndate").send_keys("31/01/2024")
driver.find_element(By.ID,"visadate").send_keys("31/01/2024")
driver.find_element(By.ID,"eamil").click()
driver.find_element(By.ID,"billing_name").send_keys("chakri siragam")
driver.find_element(By.ID,"billing_phone").send_keys("9154660350")
driver.find_element(By.ID,"billing_email").send_keys("chakri@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys("main road,k.savaram")
driver.find_element(By.ID,"billing_country").send_keys("india")
driver.find_element(By.ID,"postcode").send_keys("533126")
time.sleep(30)








