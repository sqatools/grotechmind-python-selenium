'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
a = webdriver.Chrome()
a.get('https://www.saucedemo.com/')
a.find_element(By.XPATH,"//div//input[@id='user-name']").send_keys("standard_user")
a.find_element(By.XPATH,"//div//input[@id='password']").send_keys("secret_sauce")
a.implicitly_wait(10)
a.find_element(By.XPATH,"//div//input[@id='login-button']").click()
a.implicitly_wait(10)
a.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
#a.find_element(By.XPATH,"//a[@id='inventory_sidebar_link']//following-sibling::a[text()='Reset App State']").click()
a.find_element(By.XPATH,"//head//following::nav//a[text()='All Items']").click()
a.implicitly_wait(20)
a.find_element(By.XPATH,"//div//parent::a//following::div[text()='Sauce Labs Backpack']")
a.implicitly_wait(30)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
'''
d = webdriver.Chrome()
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
d.implicitly_wait(5)
d.find_element(By.XPATH,"//div//following::input[@name='username']").send_keys("Admin")
d.find_element(By.XPATH,"//div//ancestor::div//input[@name='password']").send_keys("admin123")
d.find_element(By.XPATH,"//div//button[@type='submit']").click()
time.sleep(20)

d = webdriver.Chrome()
d.get("https://www.maxfashion.com/ae/en/")
d.implicitly_wait(5)
d.find_element(By.XPATH,"//button//span[@class='MuiButton-label' and text() = 'Sign Up' ]").click()
d.find_element(By.XPATH,"input[id='standaloneFullName']").send_keys("Chakri Siragam")
d.find_element(By.XPATH,"input[id='standalone-email']").send_keys("Chakrisiragam66@gmail.com")
d.find_element(By.XPATH,"input[id='standalone-pwd']").send_keys("Chakri@180")
d.find_element(By.XPATH,"(//span[contains(text(),'Day')])[1]").send_keys("21")
d.find_element(By.XPATH,"(//span[contains(text(),'Month')])[1]").send_keys("02")
d.find_element(By.XPATH,"//input[@name='subscribeNewsLetter' and @id='standalone-subscribe']").click()
d.find_element(By.XPATH,"class='recaptcha-checkbox-border'").click()
d.find_element(By.XPATH,"//button[@id='standalone-signup-form-submit']").click()
time.sleep(20)'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
d.find_element(By.XPATH,"//h1//following::span[contains(text(),'$200')]").click()
time.sleep(2)
d.find_element(By.XPATH,"(//div//following::input[@name='firstname'])[1]").send_keys("Chakri")
d.find_element(By.XPATH,"(//div//following::input[@name='firstname'])[2]").send_keys("Siragam")
d.find_element(By.XPATH,"//div//input[@id='birthday']").send_keys("02/21/1998")
d.find_element(By.XPATH,"//select//parent::div//input[@id='male']").click()
d.find_element(By.XPATH,"//div//ancestor::select[@id='admorepass']").send_keys(" Add 1 more passenger (100%)  ")
d.find_element(By.XPATH,"//div//input[@id='oneway']").click()
d.find_element(By.XPATH,"//div//parent::div//input[@name='fromcity']").send_keys("rajahmundary")
d.find_element(By.XPATH,"//div//parent::div//input[@name='destcity']").send_keys("hyderabad")
d.find_element(By.XPATH,"//div//input[@id='departdate']").send_keys("02/09/2024")
d.find_element(By.XPATH,"//div//input[@id='returndate']").send_keys("03/10/2024")
time.sleep(10)






















































