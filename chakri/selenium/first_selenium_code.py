'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.find_element(By.NAME,"q").send_keys("python programming")
driver.find_element(By.NAME, "btnK").click()
time.sleep(5)

driver.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(15)
driver.find_element(By.NAME,"email").send_keys("9154660350")
driver.find_element(By.NAME,"pass").send_keys("Chakri@180")
driver.find_element(By.NAME,"login").click()


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.NAME,"firstname").send_keys("Chakri")
driver.find_element(By.ID,"birthday").send_keys("21/02/1998")
driver.find_element(By.ID,"male").click()
driver.find_element(By.NAME,"fromcity").send_keys("hyderabad")
driver.find_element(By.NAME,"destcity").send_keys("rajahmundary")
driver.find_element(By.ID,"departdate").send_keys("30/01/2024")
driver.find_element(By.ID,"returndate").send_keys("31/01/2024")
driver.find_element(By.ID,"visadate").send_keys("31/01/2024")
driver.find_element(By.ID,"eamil").click()
driver.find_element(By.ID,"billing_name").send_keys("chakri siragam")
driver.find_element(By.ID,"billing_phone").send_keys("9154660350")
driver.find_element(By.ID,"billing_email").send_keys("chakri@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys("main road,k.savaram")
driver.find_element(By.ID,"billing_country").send_keys("india")
driver.find_element(By.ID,"postcode").send_keys("533126")
time.sleep(30)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"//*[@id='post-body-5123879497792889300']/div[1]/ul/li[1]/input").click()
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Chakri")
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Siragam")
driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("21/02/1998")
driver.find_element(By.XPATH,"//input[@id='male']").click()
driver.find_element(By.XPATH,"//*[@id='admorepass']").click()
driver.find_element(By.XPATH,"//*[@id='oneway']").click()
driver.find_element(By.XPATH,"//*[@id='fromcity']").send_keys('Rajahmundary')
driver.find_element(By.XPATH,"//*[@id='destcity']").send_keys('hyderabad')
driver.find_element(By.XPATH,"//*[@id='departdate']").send_keys("01/02/2024")
driver.find_element(By.XPATH,"//*[@id='returndate']").send_keys("02/02/2024")
driver.find_element(By.XPATH,"//*[@id='visadate']").send_keys("02/02.2024")
driver.find_element(By.XPATH,"//*[@id='eamil']").click()
driver.find_element(By.XPATH,"//*[@id='billing_name']").send_keys("Chakri siragam")
driver.find_element(By.XPATH,"//*[@id='billing_phone']").send_keys("9154660350")
driver.find_element(By.XPATH,"//*[@id='billing_email']").send_keys("Chakri21@gmail.comm")
driver.find_element(By.XPATH,"//*[@id='billing_address']").send_keys("main road, near mahalakshmi temple")
driver.find_element(By.XPATH,"//*[@id='billing_country']").send_keys('india')
driver.find_element(By.XPATH,"//*[@id='postcode']").send_keys("533126")
driver.find_element(By.XPATH,"//*[@id='street_address1']").send_keys("3-247,main road")
driver.find_element(By.XPATH,"//*[@id='street_address2']").send_keys("near mahalakshmi temple")
driver.find_element(By.XPATH,"//*[@id='cities']/tbody/tr[6]/td[1]/input").click()
#driver.get_screenshot_as_file('Chakri@selenium.png')
time.sleep(20)
'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/ref=nav_logo")
driver.find_element(By.XPATH,"//*[@id='nav-link-accountList']/div')]").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[@id='continue']").click()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("9154660350")
driver.find_element(By.XPATH,"//span[@id='continue']").click()
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Chakri@180")
driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d = webdriver.Chrome()
d.maximize_window()
d.get('https://www.google.com/')
d.find_element(By.XPATH,"//a[text()='Gmail']").click()
d.find_element(By.XPATH,"((//span[text()='Create an account'])[1]").click()
d.find_element(By.XPATH,"//input[contains(@aria-label,'First name')]").send_keys('chakri')
d.find_element(By.XPATH,"//input[contains(@aria-label,'Last name (optional)')]").send_keys("siragam")
d.find_element(By.XPATH,"//*[text()='Next']").click()


time.sleep(10)
'''
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

'''d = webdriver.Chrome()
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
d.implicitly_wait(10)
d.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
d.implicitly_wait(5)
d.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
d.implicitly_wait(5)
d.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
'''













