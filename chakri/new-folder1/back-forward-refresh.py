from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



'''d = webdriver.Chrome()
d.get("https://www.flipkart.com/")
d.implicitly_wait(10)
d.find_element(By.XPATH,"//span[text()='Grocery']").click()
d.back()
time.sleep(2)
d.forward()
time.sleep(2)
d.back()
d.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
a = d.find_element(By.XPATH,"(//input[@name='firstname'])[1]")
if a.is_enabled():
    a.send_keys("Chakri")
c = d.find_element(By.XPATH,"//input[@value='radio_123']")
print(c.is_enabled())
print(c.is_displayed())
print(c.is_selected())
c.click()
time.sleep(2)
print(c.is_selected())

d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
d.implicitly_wait(10)
a = d.find_element(By.ID,"admorepass")
addpass = Select(a)
addpass.select_by_visible_text("Add 2 more passenger (200%)")
time.sleep(5)
b =  d.find_element(By.ID,"billing_country")
country = Select(b)
country.select_by_visible_text("India")
time.sleep(10)

d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
d.implicitly_wait(10)
d.maximize_window()
a = d.find_element(By.XPATH,"(//table[@id='cities']//td//input[@type='checkbox'])[1]")
print(a.is_selected())
a.click()
print(a.is_selected())

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"What is Software Testing").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.find_element(By.NAME,"q").send_keys("Python")
driver.find_element(By.XPATH,"//input[@value='Search']").click()
time.sleep(3)
driver.switch_to.window(windows[0])
driver.find_element(By.LINK_TEXT,"Pytest Framework").click()
driver.find_element(By.LINK_TEXT,"Pytest- Introduction & Installation").click()
driver.find_element(By.LINK_TEXT,"Manual Testing").click()
time.sleep(3)
'''











