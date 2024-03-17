import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

'''
d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
d.implicitly_wait(10)
d.find_element(By.ID,"btnShowMsg").click()
a = Alert(d)
time.sleep(5)
print(a.text)
a.accept()

d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
d.implicitly_wait(10)
d.find_element(By.ID,"button").click()
c = Alert(d)
time.sleep(3)
#c.accept()
c.dismiss()
d = d.find_element(By.ID,"demo").text
print(d)
'''
d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
d.implicitly_wait(5)
d.find_element(By.ID,"promptbtn").click()
a = Alert(d)
#time.sleep(2)
a.send_keys("Chakri")
#time.sleep(2)
a.dismiss()
b = d.find_element(By.ID,"prompt").text
print(b)



