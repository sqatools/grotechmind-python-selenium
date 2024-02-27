import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import datetime


def get_cur_time():
    return datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.google.co.in")
# get current working directory path
cur_path = os.getcwd()
log_path1 = os.path.join(cur_path, "log")
if not os.path.isdir(log_path1):
    os.mkdir(log_path1)
log_path = os.path.join(log_path1, get_cur_time())
os.mkdir(log_path)

search_field = driver.find_element(By.NAME, "q")
# join the path with current screenshot
filename1 = f"{get_cur_time()}_search_field.png"
file_path1 = os.path.join(log_path, filename1)
search_field.screenshot(file_path1)

search_field.send_keys("Python Selenium")
search_button = driver.find_element(By.NAME, "btnK")
filename2 = f"{get_cur_time()}_search_button.png"
#search_button.screenshot(os.path.join(log_path, filename2))
search_button.click()

filename3 = f"{get_cur_time()}_searched_data.png"
driver.save_screenshot(os.path.join(log_path, filename3))

driver.get("https://www.facebook.com/")
login_button = driver.find_element(By.NAME, "login")

filename3 = f"{get_cur_time()}_searched_data.png"
login_button.screenshot(os.path.join(log_path, filename3))

time.sleep(5)

driver.close()