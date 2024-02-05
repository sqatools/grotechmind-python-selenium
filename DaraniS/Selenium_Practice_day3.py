from selenium import webdriver
from selenium.webdriver.common.by import  By
import  time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.michaelkors.com/ca/en/account/createAccount/")
driver.find_element(By.XPATH,"//input[contains(@id,'registration-form-fname')]").send_keys("Darani")
driver.find_element(By.XPATH,"//input[contains(@id,'registration-form-lname')]").send_keys("Sunkara")
driver.find_element(By.XPATH,"(//input[@id='registration-form-email'])[1]").send_keys("daranisunkara96@gmail.com")
driver.find_element(By.XPATH,"//input[@id='registration-form-password']").send_keys("Darani@123")
driver.find_element(By.XPATH,"//input[@id='registration-form-password-confirm']").send_keys("Darani@123")
driver.find_element(By.XPATH,"//input[@id='enroll-non-loyalty-customer']").click()
driver.find_element(By.XPATH,"//button[contains(text(), 'JOIN KORSVIP')]").click()

time.sleep(5)

driver.close()