from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Test_Data import *
import time

#chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
#chrome_options.add_experimental_option("prefs", prefs)

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", prefs)
# Verify that users can successfully register for a new account.

# Function to register a new account
def register_new_account(username,password,email,present=True):

	# Initialize the Selenium WebDriver
	driver= webdriver.Chrome(options = options)
	driver.maximize_window()
	driver.implicitly_wait(10)
	driver.get("https://www.irctc.co.in/")
	driver.find_element(By.XPATH,"//a[text()=' REGISTER ']").click()
	time.sleep(1)

	# UserName
	username_input = driver.find_element(By.XPATH,"//input[@id='userName']")
	username_input.send_keys(username)
	time.sleep(1)
	# Password
	Password = driver.find_element(By.XPATH,"//input[@id='usrPwd']")
	Password.send_keys(password)
	time.sleep(1)

	#confpassword
	confpassword= driver.find_element(By.XPATH,"//input[@id='cnfUsrPwd']")
	confpassword.send_keys(password)
	time.sleep(1)

	#Prefered Location
	driver.find_element(By.XPATH,"//span[text()='Preferred Language']").click()
	time.sleep(1)
	driver.find_element(By.XPATH,"//span[text()='English']").click()
	time.sleep(1)

	# Security Questions
	driver.find_element(By.XPATH,"//span[text()='Security Question']").click()
	time.sleep(1)
	driver.find_element(By.XPATH,"//span[text()='What make was your first car or bike?']").click()
	time.sleep(1)

	# Security Answer
	Security_Answer = driver.find_element(By.XPATH,"//input[@placeholder='Security Answer']")
	Security_Answer.send_keys(security_answer)

	# Click Continue
	driver.find_element(By.XPATH,"//button[text()='Continue ']").click()
	time.sleep(1)

#Personal Details
	#First Name
	first_name = driver.find_element(By.XPATH,"//input[@id='firstName']")
	first_name.send_keys(First_Name)
	time.sleep(1)

	#Last Name
	last_name = driver.find_element(By.XPATH,"//input[@id='lastname']")
	last_name.send_keys(Last_Name)
	time.sleep(1)

	# Occuption
	driver.find_element(By.XPATH,"//span[text()='Select Occupation']").click()
	time.sleep(1)
	driver.find_element(By.XPATH,"//span[text()='PROFESSIONAL']").click()
	time.sleep(1)

	# DOB
	Date_Of_Birth = driver.find_element(By.XPATH,"//input[@placeholder='Date Of Birth']")
	Date_Of_Birth.send_keys(DOB)
	time.sleep(1)
	# Relationship
	driver.find_element(By.XPATH,"//label[text()='Married']").click()
	time.sleep(1)

	# Country

	time.sleep(1)
	static_dropdown = driver.find_element(By.XPATH,"//select[@formcontrolname='resCountry']")
	select = Select(static_dropdown)
	select.select_by_visible_text("Select a Country")
	time.sleep(2)
	select.select_by_visible_text("India")

	# gander
	driver.find_element(By.XPATH,"//span[text()='Male']").click()
	time.sleep(1)

	# Email
	Email = driver.find_element(By.XPATH,"//input[@id='email']")
	Email.send_keys(email)
	time.sleep(1)

	# Mobile
	mobile = driver.find_element(By.XPATH,"//input[@id='mobile']")
	mobile.send_keys(Mobile)
	time.sleep(1)

	# Nationality
	Select_Dropdown= driver.find_element(By.XPATH,"//select[@formcontrolname='nationality']")
	select=Select(Select_Dropdown)
	select.select_by_visible_text("India")
	time.sleep(1)

	# Click on Continue
	driver.find_element(By.XPATH,"//button[text()='Continue ']").click()
	time.sleep(1)

# Address
	#Flat/Block No
	flat = driver.find_element(By.XPATH,"//input[@id='resAddress1']")
	flat.send_keys(Flat)
	time.sleep(1)

	#Street
	street = driver.find_element(By.XPATH,"//input[@id='resAddress2']")
	street.send_keys(Street)
	time.sleep(1)

	# Area
	area = driver.find_element(By.XPATH,"//input[@id='resAddress3']")
	area.send_keys(Area)
	time.sleep(1)

	# Pin code
	pincode = driver.find_element(By.XPATH,"//input[@placeholder='Pin code']")
	pincode.send_keys(PinCode)
	time.sleep(1)

	# City
	driver.find_element(By.XPATH,"//div[@id='ui-tabpanel-2']//div[5]").click()
	select_city= driver.find_element(By.XPATH,"//select[@formcontrolname='resCity']")
	select = Select(select_city)
	select.select_by_value("New Delhi")
	time.sleep(1)

	# Post Office
	post_office = driver.find_element(By.XPATH,"//select[@formcontrolname='resPostOff']")
	select1 = Select(post_office)
	select1.select_by_value("New Delhi G.P.O. ")
	time.sleep(1)

	#Phone
	phone = driver.find_element(By.XPATH,"//input[@id='resPhone']")
	phone.send_keys(Mobile)
	time.sleep(1)

	# Copy Residence to Office Address
	driver.find_element(By.XPATH,"//label[text()='Yes']").click()
	time.sleep(20)

	# Enter Captcha
	captcha = driver.find_element(By.XPATH,"//input[@id='captcha']")
	captcha.send_keys(Captcha)
	time.sleep(1)

	# Click on Register Button
	driver.find_element(By.XPATH,"//button[text()='REGISTER']").click()
	time.sleep(1)

register_new_account(username,password,email)

#def login_with_Valied_Cred(username, password):


