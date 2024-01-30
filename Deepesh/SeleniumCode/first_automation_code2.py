"""
 pip install selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#driver = webdriver.Chrome()

# initiating the browser driver
driver = webdriver.Edge()

# maximizing the browser window
driver.maximize_window()
# set timeout for each of the element on the browser
driver.implicitly_wait(10)
# provide url of server/website to be launched.
driver.get("https://www.facebook.com/")
# provide element locator to intract with the element
driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "pass").send_keys("admin@123")
driver.find_element(By.NAME, "login").click()

time.sleep(5)

driver.close()




