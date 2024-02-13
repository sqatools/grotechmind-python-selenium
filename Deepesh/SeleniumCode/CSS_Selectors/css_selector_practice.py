"""
CSS Selector:

ID :
   tagname#element_id
   input#fromcity

CLASS :
   tagname.element_class_name
   h3.post-title.entry-title

Attribute:
      tagname[attribute='value']
      input[value='radio_345']
      input[id='male']
      li[data-cy='oneWayTrip']

substring
      tagname[attrribute*='partial value']
      li[data-cy*='oneWay']
      li[data-cy*='round']
      input[data-cy*='from']

Element traversing:
       div[id='billing_details']>input[id='billing_name']
       div[id='billing_details']>input#billing_name
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.CSS_SELECTOR, "div[id='billing_details']>input#billing_name").send_keys("John Doew")
time.sleep(5)
driver.close()
