from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
#driver.find_element(By.XPATH,"//*[@id="APjFqb"]").send_keys("name")
#driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
