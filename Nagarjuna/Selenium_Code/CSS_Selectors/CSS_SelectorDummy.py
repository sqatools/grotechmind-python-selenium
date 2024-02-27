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

title = driver.find_element(By.CSS_SELECTOR,"h3.post-title.entry-title").text
print(title)  #with class and printing the title
              # Dummy Website
page_title = driver.find_element(By.CSS_SELECTOR,"h1[align='center']").text
print(page_title) # with attribute and printing
                  # Dummy Ticket Booking Website
module_1 =driver.find_element(By.XPATH,"//h3[text()='Choose the correct option:']").text
print(module_1)  # with xpath unable to get CSS and printing
                 # Choose the correct option:

driver.find_element(By.CSS_SELECTOR,"input[value='radio_123']").click()

visa_application = driver.find_element(By.XPATH,"//span[text()='Dummy ticket for visa application - $200 ']").text
print(visa_application)     #

driver.find_element(By.CSS_SELECTOR,"input[value='radio_345']").click()

return_ticket = driver.find_element(By.XPATH,"//span[text()='Dummy return ticket - $300 ']").text
print(return_ticket)

driver.find_element(By.CSS_SELECTOR,"input[value='radio_678']").click()

hotel_ticket = driver.find_element(By.XPATH,"//span[text()='Dummy hotel booking ticket - $400 ']").text
print(hotel_ticket)

driver.find_element(By.XPATH,"(//input[@value='radio_558'])[1]").click()

flight_ticket = driver.find_element(By.XPATH,"//span[text()='Dummy hotel  and flight booking - $500 ']").text
print(flight_ticket)

driver.find_element(By.XPATH,"(//input[@value='radio_558'])[2]").click()

cab_booking = driver.find_element(By.XPATH,"//span[text()='Cab booking and return date - $600 ']").text
print(cab_booking)



time.sleep(5)
driver.close()
