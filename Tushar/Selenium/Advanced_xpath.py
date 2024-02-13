"""
from selenium import webdriver
from selenium.webdriver.common.by import By
#import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")
#driver.find_element(By.XPATH,"//span[text()='From']//following::input").send_keys('Pune')
#driver.find_element(By.XPATH,"//span[text()='From']//following::input").send_keys('Nashik')

fromcity=driver.find_element(By.XPATH,"//span[text()='From']").text
print(fromcity)
#driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::input").send_keys('Mumbai')

entercity=driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p").text
print(entercity)
#driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::input").send_keys('hyd')

driver.find_element(By.XPATH,"//p[text()='9']//parent::div[contains(@aria-label,'Feb')]").click()

#//span[contains(text(),'SEARCH FLIGHTS')]

time.sleep(5)
driver.close()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.makemytrip.com/")

x=driver.find_element(By.XPATH,"//p[text()='Student ']//parent::li").text
print(x)

driver.find_element(By.XPATH,"//span[@class='chNavIcon appendBottom2 chSprite chTrains']").click()
driver.find_element(By.XPATH,"//span[@class='chNavIcon appendBottom2 chSprite chCabs']").click()


time.sleep(5)
driver.close()
