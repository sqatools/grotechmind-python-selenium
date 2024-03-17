from selenium.webdriver.common.by import By
import time
from test_data import *

def test_fb_login(browser):
    browser.get(fb_url)
    browser.find_element(By.XPATH,"//input[@name='email']").send_keys('abc@gmail.com')
    browser.find_element(By.XPATH,"//input[@id='pass']").send_keys('12345')
    browser.find_element(By.XPATH,"//button[@name='login']").click()

time.sleep(5)


def test_pass_reset(browser):
    browser.get(fb_url)
    browser.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
    browser.find_element(By.XPATH,"//input[@id='identify_email']").send_keys('1234567890')
    browser.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(5)

