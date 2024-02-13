"""
implicit wait : when we apply implicit wait
then it apply on all the web element of the website
and wait up to max value defined to find the element.

explicit wait : This wait will apply on specific element
of the web page, user can mention any specified to be satisfied.

fluent wait : when user change the polling frequency of explicit
wait , then it is known as fluent wait.

static wait : It is also known as hard sleep, script has to wait
    un-till specified time.
    time.sleep(5)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15, poll_frequency=2) # explicit wait

driver.get("https://www.facebook.com/")

print("website title:", driver.title)
print("website  url :", driver.current_url)

t1 = time.time()
try:

    wait.until(ec.url_contains("facebook"))
    status = wait.until(ec.text_to_be_present_in_element((By.XPATH, "//a[@data-testid='open-registration-form-button']"), "Create new account"))
    print("status :", status)
except Exception as e:
    print(e)
t2 = time.time()
print("time diff :", t2-t1)


