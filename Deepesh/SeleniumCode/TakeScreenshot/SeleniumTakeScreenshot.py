import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.google.co.in")
# get current working directory path
cur_path = os.getcwd()
log_path = os.path.join(cur_path, "log")

search_field = driver.find_element(By.NAME, "q")
# join the path with current screenshot
file_path1 = os.path.join(log_path, "search_field.png")
search_field.screenshot(file_path1)

search_field.send_keys("Python Selenium")
search_button = driver.find_element(By.NAME, "btnK")
file_path2 = os.path.join(log_path, "search_button.png")
#search_button.screenshot(file_path2)
search_button.click()

#file_path3 = os.path.join(cur_path, "search_button.png")
driver.save_screenshot(os.path.join(log_path, "searched_data.png"))

driver.get("https://www.facebook.com/")
login_button = driver.find_element(By.NAME, "login")

login_button.screenshot(os.path.join(log_path, "facebook_login_btn.png"))

time.sleep(5)

driver.close()