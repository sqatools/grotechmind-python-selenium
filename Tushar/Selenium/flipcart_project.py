from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH,"//a[text()='Login']").click()
driver.find_element(By.XPATH,"(//input[@type='text' and @autocomplete='off'])[2]").click()
driver.find_element(By.XPATH,"(//input[@type='text' and @autocomplete='off'])[2]").send_keys('tusharaher3131@gmail.com')
driver.find_element(By.XPATH,"//button[text()='Request OTP']").click()











time.sleep(5)
driver.close()
