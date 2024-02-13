from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

"""
Methods we have covered in this script
back() : go back to previous page
forward() : move forward to old page.
refresh() : refresh the browser page.
is_enabled() : check for element is enabled
is_displayed() : check for element is displayed.
is_selected() : check for element is selected or not
                for radio button and checkbox.
                
            

"""
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.find_element(By.XPATH, "//span[text()='Grocery']").click()
element = driver.find_element(By.XPATH, "//a[contains(@href, 'GROCERY')]/img")
assert element
time.sleep(3)
driver.back()
# driver.find_element(By.XPATH, "//span[text()='Mobiles']").click()
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)

# navigate to other website
driver.get("https://www.facebook.com")

username_field = driver.find_element(By.ID, "email")
print("check for displayed :", username_field.is_displayed())
print("check for enabled :", username_field.is_enabled())

if username_field.is_enabled():
    username_field.send_keys("admin")

password = driver.find_element(By.ID, "pass")
if password.is_enabled():
    password.send_keys("Admin@123")

# check for element is selected or not
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.refresh()
male_radio_btn = driver.find_element(By.ID, "male")
print("check element is selected :", male_radio_btn.is_selected())
male_radio_btn.click()
print("check element is selected :", male_radio_btn.is_selected())

time.sleep(3)

check_box = driver.find_element(By.XPATH, "//td[text()='Pune']//parent::tr//input")
print("check element is selected :", check_box.is_selected())
check_box.click()
print("check element is selected :", check_box.is_selected())

time.sleep(5)
driver.close()
