from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.webdriver.support.wait import wait
import time


#1 Verify that users can successfully register for a new account.
'''
d = webdriver.Chrome()
d.get("https://www.booking.com/")
d.implicitly_wait(15)
d.find_element(By.XPATH,"//span[text()='Register']").click()
d.find_element(By.NAME,"username").send_keys("chakri9154@gmail.comgmail.com")
d.find_element(By.XPATH,"//button[@type='submit']").click()
d.find_element(By.NAME,"new_password").send_keys("Chakri@180")
d.find_element(By.NAME,"confirmed_password").send_keys("Chakri@180")
d.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
print("New Account successfully created")


'''
# 2 Validate the login functionality with valid credentials.

d = webdriver.Chrome()
d.get("https://www.booking.com/")
d.implicitly_wait(15)
d.find_element(By.XPATH,"(//span[text()='Sign in'])[1]").click()
d.find_element(By.NAME,"username").send_keys("chakri9154@gmail.com")
d.find_element(By.XPATH,"//button[@type='submit']").click()
d.find_element(By.XPATH,"//input[@id='password']").send_keys("Chakri@180")
d.find_element(By.XPATH,"//button[@type='submit']").click()
print("successfully logged in")


'''#3 Test login with invalid credentials and ensure proper error messages are displayed.

d = webdriver.Chrome()
d.get("https://www.booking.com/")
d.implicitly_wait(15)
d.find_element(By.XPATH,"(//span[text()='Sign in'])[1]").click()
d.find_element(By.NAME,"username").send_keys("chakri9154@gmail.com")
d.find_element(By.XPATH,"//button[@type='submit']").click()
d.find_element(By.XPATH,"//input[@id='password']").send_keys("Chakri@181")
d.find_element(By.XPATH,"//button[@type='submit']").click()
a = d.find_element(By.XPATH,"//div[@id='password-note']").text
print(a)

time.sleep(10)
d.close()

'''
#4 Test the search functionality for one-way flights.
d.find_element(By.XPATH,"//div[text()='I’m looking for flights']").click()
time.sleep(10)
a = d.find_element(By.NAME,"ss")
airport = Select(a)
airport.select_by_visible_text("Goa")
time.sleep(5)

