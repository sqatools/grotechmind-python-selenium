import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
frame_element = driver.find_element(By.NAME, "globalSqa")
driver.switch_to.frame(frame_element)
phone_number = driver.find_element(By.XPATH, "//div[@class='header_phone']").text
print("Phone Number :", phone_number)
email_id = driver.find_element(By.XPATH, "//div[@class='header_mail']").text
print("email id :", email_id)
time.sleep(5)
driver.find_element(By.XPATH, "//img[@alt='Selenium Online Training']").click()

time.sleep(5)

driver.find_element(By.XPATH, "//div[@id='mobile_menu_toggler']").click()
time.sleep(5)

# moving out of the iframe
driver.switch_to.default_content()

driver.find_element(By.XPATH, "//li[@id='menu-item-1561']//a[text()='Contact Us']").click()
time.sleep(5)
driver.close()