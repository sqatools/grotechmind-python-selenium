from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

From = "New Delhi"
Destination = "Bangalore"

driver.get("https://www.goibibo.com/")
time.sleep(1)

driver.find_element(By.XPATH,"//span[@role='presentation']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p[text()='Enter city or airport']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']").send_keys(From)
time.sleep(1)

driver.find_element(By.XPATH,"//p[text()='Indira Gandhi International Airport']//ancestor::li[@role='presentation']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']").send_keys(Destination)
time.sleep(1)

driver.find_element(By.XPATH,"//span[text()='Bengaluru, India']//ancestor::li[@role='presentation']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//p[text()='9']//following-sibling::p[@class='fsw__price ']").click()
time.sleep(1)

