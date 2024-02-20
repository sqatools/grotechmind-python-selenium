from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = "chrome"

if browser =="edge":
    driver = webdriver.Edge()
elif browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("nagarjuna")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("22435")

time.sleep(4)
driver.close()
