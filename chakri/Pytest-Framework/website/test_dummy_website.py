import time
from selenium.webdriver.common.by import By
from test_data import *

def test_dummy(website):
    website.get(url)
    website.find_element(By.NAME,"firstname").send_keys("Chakri")
    website.find_element(By.ID,"birthday").send_keys("21/02/1998")
    website.find_element(By.ID,"male").click()
    website.find_element(By.NAME,"fromcity").send_keys("hyderabad")
    website.find_element(By.NAME,"destcity").send_keys("rajahmundary")
    website.find_element(By.ID,"departdate").send_keys("30/01/2024")
    website.find_element(By.ID,"returndate").send_keys("31/01/2024")
    website.find_element(By.ID,"visadate").send_keys("31/01/2024")
    website.find_element(By.ID,"eamil").click()
    website.find_element(By.ID,"billing_name").send_keys("chakri siragam")
    website.find_element(By.ID,"billing_phone").send_keys("9154660350")
    website.find_element(By.ID,"billing_email").send_keys("chakri@gmail.com")
    website.find_element(By.ID,"billing_address").send_keys("main road,k.savaram")
    website.find_element(By.ID,"billing_country").send_keys("india")
    website.find_element(By.ID,"postcode").send_keys("533126")
    time.sleep(30)
