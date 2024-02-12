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
# driver.implicitly_wait(10)  # implicit wait
# wait = WebDriverWait(driver, 15) # explicit wait
wait = WebDriverWait(driver, 15, poll_frequency=2) # explicit wait

driver.get("https://www.google.co.in")
t1 = time.time()
try:
    driver.find_element(By.NAME, "q").send_keys("Python Programming")
except Exception as e:
    print(e)

t2 = time.time()
print("difference :", t2-t1)



p1 = time.time()
try:
    element = wait.until(ec.visibility_of_element_located((By.NAME, "btnK")))
    element.click()
except Exception as e:
    print(e)
p2 = time.time()

print("time difference :", p2-p1)

#driver.find_element(By.NAME, "btnK").click()

time.sleep(20) # static wait.

driver.close()