##Text Method:
# //tagname[text()='text value']

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#driver.get("https://www.flipkart.com/")

#driver.find_element(By.XPATH, "//input[@type= 'text']").send_keys('mobile')
#driver.find_element(By.XPATH,"//img[@alt= 'Grocery']").click()
#driver.find_element(By.XPATH,"//input[@title='Enter pincode'][1]").send_keys(422216)
#driver.find_element(By.XPATH,"//img[@title='Flipkart']").click()
#driver.find_element(By.XPATH,"//span[text()='Electronics']").click()
#driver.find_element(By.XPATH,"//span[contains text(),'TV']").click()
#driver.find_element(By.XPATH,"//span[text()='Men']").click()
#driver.find_element(By.XPATH,"//span[text()='Grocery']").click()


# driver.find_element(By.XPATH,"//input[@id='billing_email']//following::input[@type='checkbox'][3]").click()
# driver.find_element(By.XPATH,"//input[@id='billing_name']//following::input[@id='billing_phone']").send_keys('9860560531')
# driver.find_element(By.XPATH,"//select[@id='admorepass']//following::input[@id='departdate']").send_keys('04-02-2024')
# driver.find_element(By.XPATH,"//span[text()='Email']//following::span[text()='WhatsApp']").click()
# driver.find_element(By.XPATH,"//input[@id='billing_address']//following::input[@id='street_address1']").send_keys('Pune')

#driver.find_element(By.XPATH,"//input[@id='billing_name']//following-sibling::input[@id='billing_address']").send_keys('nashik')
#v=driver.find_element(By.XPATH,"//input[@id='visadate']//following-sibling::h2[2]").text
#print(v)

#//input[@name='postcode']//parent::div
#//input[@id='billing_name']//parent::div[@id='billing_details']
#//input[@id='billing_name']//ancestor::*









time.sleep(5)
driver.close()



