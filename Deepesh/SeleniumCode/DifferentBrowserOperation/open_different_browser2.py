from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def open_facebook(driver):
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, "email").send_keys("admin_user")
    driver.find_element(By.ID, "pass").send_keys("Admin@123")

    time.sleep(5)
    driver.close()

browser_list = [
    webdriver.Chrome(),
    webdriver.Firefox(),
    webdriver.Edge(),
]

for driver in browser_list:
    open_facebook(driver)