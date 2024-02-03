from selenium import webdriver
from selenium.webdriver.common.by import  By
import  time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Darani")
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Sunkara")
driver.find_element(By.XPATH,"//*[@id='birthday']").send_keys("03/08/1996")
driver.find_element(By.XPATH,"(//*[@id='female'])[1]").click()
#driver.find_element(By.XPATH,"/*[@id='oneway']").click()
driver.find_element(By.XPATH,"//*[@id='fromcity']").send_keys("Canada")
driver.find_element(By.XPATH,"//*[@id='destcity']").send_keys("India")
driver.find_element(By.XPATH,"//*[@id='departdate']").send_keys("31/01/2024")
driver.find_element(By.XPATH,"//*[@id='returndate']").send_keys("22/02/2024")
driver.find_element(By.XPATH,"//*[@id='visadate']").send_keys("02/02/2024")
#driver.find_element(By.XPATH,"(//*[@id='female'])[2]").click()
driver.find_element(By.XPATH,"//*[@id='billing_name']").send_keys("Darani")
driver.find_element(By.XPATH,"//*[@id='billing_phone']").send_keys("6389944297")
driver.find_element(By.XPATH,"//*[@id='billing_email']").send_keys("Darani@gmail.com")
driver.find_element(By.XPATH,"//*[@id='billing_address']").send_keys("3925,adnnfm")




time.sleep(5)

driver.close()