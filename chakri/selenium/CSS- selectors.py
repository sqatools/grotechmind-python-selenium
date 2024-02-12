from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

'''d = webdriver.Chrome()
d. get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
a = d.find_elements(By.XPATH,"//div[@align='left']//ul//li//input")
for i in a:
    i.click()
    d.implicitly_wait(5)
    print(i.text)
'''
d = webdriver.Chrome()
d.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
d.find_element(By.CSS_SELECTOR,"input[value='radio_123']").click()
d.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Chakri")
d.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Siragam")
d.find_element(By.CSS_SELECTOR,"input#birthday").send_keys("02/21/1998")
d.find_element(By.CSS_SELECTOR,"input#male").click()
d.find_element(By.CSS_SELECTOR,"select[id='admorepass']").send_keys("add 1 more passenger")
d.find_element(By.CSS_SELECTOR,"input#oneway").click()
d.find_element(By.CSS_SELECTOR,"input[name*='from']").send_keys("rajahmundary")
d.find_element(By.CSS_SELECTOR,"input[name*='dest']").send_keys("hyderabad")
d.find_element(By.CSS_SELECTOR,"input[name*='depart']").send_keys("02/11/2024")
d.find_element(By.CSS_SELECTOR,"input[name*='return']").send_keys("02/13/204")
d.find_element(By.CSS_SELECTOR,"input[name*='visa']").send_keys("02/12/2024")
d.find_element(By.XPATH,"(//input[@id='female'])[2]").click()
d.find_element(By.CSS_SELECTOR,"div[id='billing_details']>input[id='billing_name']").send_keys("Chakri Siragam")
d.find_element(By.CSS_SELECTOR,"div[id='billing_details']>input[id='billing_phone']").send_keys("9154660350")
d.find_element(By.CSS_SELECTOR,"div[id='billing_details']>input[id='billing_email']").send_keys("Chakri@gmail.com")
d.find_element(By.CSS_SELECTOR,"div[id='billing_details']>input[id='billing_address']").send_keys("K.savaram")
d.find_element(By.CSS_SELECTOR,"select#billing_country").send_keys("india")
d.find_element(By.CSS_SELECTOR,"input#postcode").send_keys("533126")
d.find_element(By.CSS_SELECTOR,"input#street_address1").send_keys("main road")
a = d.find_elements(By.XPATH,"//table[@id='cities']//input[@type='checkbox']")
for i in a:
    i.click()

b = d.find_elements(By.XPATH,"//table[@id='cities']//td[3]")
for city in b:
    print(city.text)




