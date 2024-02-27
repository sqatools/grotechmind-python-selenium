from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")

# driver.find_element(By.XPATH,"//div[@id='nav-tools']//following-sibling::a[@data-nav-role='signin']").click()
# driver.find_element(By.XPATH,"//input[@name='email']").click()
# driver.find_element(By.XPATH,"//input[@name='email']").send_keys('tusharaher3131@gmail.com')
# driver.find_element(By.XPATH,"//input[@id='continue']").click()

#2)Verify login is successful with correct email and password.################

driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
driver.find_element(By.XPATH,"//input[@name='email']").click()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys('tusharaher3131@gmail.com')
driver.find_element(By.XPATH,"//input[@id='continue']").click()
driver.find_element(By.XPATH,"//input[@name='password']").click()
driver.find_element(By.XPATH,"//input[@name='password']").send_keys('Pratu@5412')
driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()

#3) Ensure login fails with incorrect email or password.

#sign out

#driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
#driver.find_element(By.XPATH,"//span[text()='Sign Out']").click()

#login

driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
driver.find_element(By.XPATH,"//input[@name='email']").click()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys('tusharaher3131@gmail.com')
driver.find_element(By.XPATH,"//input[@id='continue']").click()
driver.find_element(By.XPATH,"//input[@name='password']").click()
driver.find_element(By.XPATH,"//input[@name='password']").send_keys('Pratu@54123')
driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()


time.sleep(5)
#driver.close()
time.sleep(5)
