from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.find_element(By.NAME,"q").send_keys("Python Programming")
driver.find_element(By.NAME,"btnk").click()
time.sleep(10)
driver.close()"""


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.ID,"firstname").send_keys("Ankita")
driver.find_element(By.ID,"LastName").send_keys("Verma")
driver.find_element(By.ID,"male").click()
driver.find_element(By.ID,"birthday").send_keys("01.09.1995")
driver.find_element(BY.ID,"admorepass").send_keys(" Add 2 more passenger (200%) ")
driver.find_element(BY.ID,"")
time.sleep(10)
driver.find_element(By.ID,"")
driver.maximize_window()



driver.close()
