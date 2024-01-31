from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.ID,"firstname").send_keys("Ankita")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@name='firstname'])[2]").send_keys("Verma")
time.sleep(1)
driver.find_element(By.ID, "female").click()
time.sleep(1)
#driver.find_element(By.XPATH,"(//[@id='admorepass'])[3]").send_keys("Add 2 more passenger (200%)")
#//*[@id="admorepass"]
driver.find_element(By.ID,"roundtrip").click()
time.sleep(1)
driver.find_element(By.ID,"fromcity").send_keys("Delhi")
time.sleep(1)
driver.find_element(By.ID,"destcity").send_keys("Mumbai")
time.sleep(1)
driver.find_element(By.ID,"departdate").send_keys("09-11-2023")
time.sleep(1)
driver.find_element(By.ID,"returndate").send_keys("12-11-2023")
time.sleep(1)
driver.find_element(By.ID,"visadate").send_keys("12-04-2024")

driver.find_element(By.ID,"whatsapp").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@id='billing_name'])").send_keys("Ankita")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@id='billing_phone'])").send_keys("23445877")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@id='billing_email'])").send_keys("AV@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@id='billing_address'])").send_keys("Street 7 ")
time.sleep(1)
#Drop down???
#driver.find_element(By.XPATH, "(//input[@id='billing_country'])").send_keys("India")
driver.find_element(By.XPATH,"(//input[@id='street_address1'])").send_keys("India ")
time.sleep(1)
driver.close()
