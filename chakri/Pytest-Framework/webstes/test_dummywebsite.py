import time
from selenium.webdriver.common.by import By
from ..test_data import *


def test_dummy_website(browser):
    browser.get(url)
    browser.find_element(By.NAME,"firstname").send_keys("Chakri")
    browser.find_element(By.ID,"birthday").send_keys("21/02/1998")
    browser.find_element(By.ID,"male").click()
    browser.find_element(By.NAME,"fromcity").send_keys("hyderabad")
    browser.find_element(By.NAME,"destcity").send_keys("rajahmundary")
    browser.find_element(By.ID,"departdate").send_keys("30/01/2024")
    browser.find_element(By.ID,"returndate").send_keys("31/01/2024")
    browser.find_element(By.ID,"visadate").send_keys("31/01/2024")
    browser.find_element(By.ID,"eamil").click()
    browser.find_element(By.ID,"billing_name").send_keys("chakri siragam")
    browser.find_element(By.ID,"billing_phone").send_keys("9154660350")
    browser.find_element(By.ID,"billing_email").send_keys("chakri@gmail.com")
    browser.find_element(By.ID,"billing_address").send_keys("main road,k.savaram")
    browser.find_element(By.ID,"billing_country").send_keys("india")
    browser.find_element(By.ID,"postcode").send_keys("533126")
