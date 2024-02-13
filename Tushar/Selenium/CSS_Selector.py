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

web_name=driver.find_element(By.CSS_SELECTOR,"h3.post-title.entry-title").text #using class
print(web_name)   #Dummy Website

dummy_web=driver.find_element(By.CSS_SELECTOR,"h1[align='center']").text  #using attribute
print(dummy_web)   #Dummy Ticket Booking Website

option=driver.find_element(By.XPATH,"//h3[text()='Choose the correct option:']").text
print(option)  #Choose the correct option:

driver.find_element(By.CSS_SELECTOR,"input[value='radio_123']").click()

visa_application=driver.find_element(By.XPATH,"//span[text()='Dummy ticket for visa application - $200 ']").text
print(visa_application)

driver.find_element(By.CSS_SELECTOR,"input[value='radio_345']").click()

return_ticket=driver.find_element(By.XPATH,"//span[text()='Dummy return ticket - $300 ']").text
print(return_ticket)

driver.find_element(By.CSS_SELECTOR,"input[value='radio_678']").click()

hotel_ticket=driver.find_element(By.XPATH,"//span[text()='Dummy hotel booking ticket - $400 ']").text
print(hotel_ticket)

driver.find_element(By.XPATH,"(//input[@value='radio_558'])[1]").click()

flight_booking=driver.find_element(By.XPATH,"//span[text()='Dummy hotel  and flight booking - $500 ']").text
print(flight_booking)

driver.find_element(By.XPATH,"(//input[@value='radio_558'])[2]").click()

cab_booking=driver.find_element(By.XPATH,"//span[text()='Cab booking and return date - $600 ']").text
print(cab_booking)

pass_det=driver.find_element(By.XPATH,"//h2[text()='Passenger Details']").text
print(pass_det)

driver.find_element(By.XPATH,"( //input[@name='firstname'])[1]").send_keys('Tushar')
driver.find_element(By.XPATH,"( //input[@name='firstname'])[2]").send_keys('Aher')

driver.find_element(By.CSS_SELECTOR,"input#birthday").send_keys('10/08/1989')
driver.find_element(By.CSS_SELECTOR,"input#male").click()
driver.find_element(By.XPATH,"(//input[@id='female'])[1]").click()












time.sleep(5)
driver.close()
