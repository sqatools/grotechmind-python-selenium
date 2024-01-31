"""
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
"""
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
src = "Mumbai"
dest = "Bangalore"

# Identify by ID
website_name = driver.find_element(By.CLASS_NAME, "post-title entry-title").text
print("website name text :", website_name)
driver.find_element(By.ID, "fromcity").send_keys(src)
driver.find_element(By.ID, "destcity").send_keys(dest)
header = driver.find_element(By.TAG_NAME, "h1").text
print(header)
"""

# driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
#driver.find_element(By.LINK_TEXT, "What is Software Testing").click()

#driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
#driver.find_element(By.PARTIAL_LINK_TEXT, "Black").click()

driver.get("https://www.google.co.in")
driver.find_element(By.NAME, "q").send_keys("Python Programming")
driver.find_element(By.NAME, "btnK").click()
driver.find_element(By.LINK_TEXT, "Python For Beginners").click()

time.sleep(5)
driver.close()



