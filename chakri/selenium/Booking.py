from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import wait
import time


#1 Verify that users can successfully register for a new account.

d = webdriver.Chrome()
d.get("https://www.booking.com/")
d.implicitly_wait(15)
d.find_element(By.XPATH,"//span[text()='Register']").click()
d.find_element(By.NAME,"username").send_keys("Chakrisiragam66@gmil.com")
d.find_element(By.XPATH,"//button[@type='submit']").click()
d.find_element(By.NAME,"new_password").send_keys("Chakri@180")
d.find_element(By.NAME,"confirmed_password").send_keys("Chakri@180")
d.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
print("New Account successfully created")
