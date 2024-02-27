import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")

# Alert box
"""
driver.find_element(By.ID, "btnShowMsg").click()
time.sleep(2)
wait.until(ec.alert_is_present())
alert_obj = Alert(driver)
print("alert msg :", alert_obj.text)
alert_obj.accept()
"""

# Confirm Box
"""
driver.find_element(By.ID, "button").click()
time.sleep(3)
alert = Alert(driver)
# alert.accept()
# accept_msg = driver.find_element(By.ID, "demo").text
# print("msg from UI :", accept_msg)
# assert accept_msg == "You pressed OK!"

alert.dismiss()
accept_msg = driver.find_element(By.ID, "demo").text
print("msg from UI :", accept_msg)
assert accept_msg == "You pressed Cancel!"
"""


# prompt box
driver.find_element(By.ID, "promptbtn").click()
time.sleep(4)
alert = Alert(driver)
alert.send_keys("GrowTechMind")
alert.accept()

ui_msg = driver.find_element(By.ID, "prompt").text
print("UI message :", ui_msg)
time.sleep(4)
assert ui_msg == f"Hello GrowTechMind! How are you today?"



time.sleep(5)
driver.close()