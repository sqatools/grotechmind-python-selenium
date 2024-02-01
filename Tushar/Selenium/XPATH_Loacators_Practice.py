"""
xpath :

1). Absolute XPATH:
/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/ul/li[5]/a

2). Relative XPATH:
      i)   //tagname[@attribute='value']
           //input[@name='fromcity']
           //input[@id='fromcity']
           //input[@fdprocessedid='avj1c4']

      ii) //*[@attribute='value']
          //*[@fdprocessedid='avj1c4']

     iii) multiple element with same attribute : (//tagname[@attribute='value'])[1]
          (//input[@name='firstname'])[2]



"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.XPATH, "(//input[@name='firstname'])[1]").send_keys("Tushar")
driver.find_element(By.XPATH, "(//input[@name='firstname'])[2]").send_keys("Aher")
driver.find_element(By.XPATH,"//input[@name='birthday']").send_keys('10-08-1989')
driver.find_element(By.XPATH,"//input[@id='male']").click()
driver.find_element(By.XPATH,"//input[@id='female']").click()
driver.find_element(By.XPATH,"//*[@id='admorepass']").click()
driver.find_element(By.XPATH,"//*[@name='fromcity']").send_keys("nashik")
driver.find_element(By.XPATH,"//*[@name='destcity']").send_keys('pune')
driver.find_element(By.XPATH,"//*[@id='departdate']").send_keys('31-01-2024')
driver.find_element(By.XPATH,"//*[@id='returndate']").send_keys("15-02-2024")
driver.find_element(By.XPATH,"//*[@id='visadate']").send_keys('25-02-2024')
time.sleep(5)

driver.close()

# //*[@attribute='value']
#//*[@fdprocessedid='avj1c4']


