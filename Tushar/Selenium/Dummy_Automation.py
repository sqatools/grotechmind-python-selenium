from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

website_name=driver.find_element(By.XPATH,"//h1[contains(text(),' Dummy Ticket Booking Website')]").text
print("website name:",website_name) #website name: Dummy Ticket Booking Website

radio1=driver.find_element(By.XPATH,"//*[contains(text(),'Dummy ticket for visa application - $200 ')]").text
print(radio1) #Dummy ticket for visa application - $200
driver.find_element(By.XPATH,"//input[@value='radio_123']").click()

radio2=driver.find_element(By.XPATH,"//span[text()='Dummy return ticket - $300 ']").text
print(radio2) #Dummy return ticket - $300
driver.find_element(By.XPATH,"//input[@value='radio_345']").click()

radio3=driver.find_element(By.XPATH,"//span[text()='Dummy hotel booking ticket - $400 ']").text
print(radio3) #Dummy hotel booking ticket - $400
driver.find_element(By.XPATH,"//input[@value='radio_678']").click()

radio4=driver.find_element(By.XPATH,"//span[text()='Dummy hotel  and flight booking - $500 ']").text
print(radio4) #Dummy hotel and flight booking - $500
driver.find_element(By.XPATH,"(//input[@value='radio_558'])[1]").click()

radio5=driver.find_element(By.XPATH,"//span[text()='Cab booking and return date - $600 ']").text
print(radio5) #Cab booking and return date - $600
driver.find_element(By.XPATH,"(//input[@value='radio_558'])[2]").click()

passenger=driver.find_element(By.XPATH,"//h2[text()='Passenger Details']").text
print('passenger:',passenger) #Passenger Details

first_name=driver.find_element(By.XPATH,"//span[text()='    First Name    ']").text
print(first_name)
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys('Tushar')

last_name=driver.find_element(By.XPATH,"//span[text()='    Last Name     ']").text
print(last_name)
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys('Aher')

DOB=driver.find_element(By.XPATH,"//span[text()='Date of birth*']").text
print(DOB)
driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys('10/08/1989')

sex=driver.find_element(By.XPATH,"//span[text()='Sex*']").text
print(sex)
driver.find_element(By.XPATH,"//input[@id='male']").click()
male=driver.find_element(By.XPATH,"//span[text()='Male']").text
print(male)
driver.find_element(By.XPATH,"(//input[@id='female'])[1]").click()
female=driver.find_element(By.XPATH,"//span[text()='Female']").text
print(female)

Add_passangers=driver.find_element(By.XPATH,"//h3[text()=' Number of Additional Passangers']").text
print(Add_passangers)

driver.find_element(By.XPATH,"//select[@id='admorepass']").click()

travel=driver.find_element(By.XPATH,"//h2[text()=' Travel Details ']").text
print(travel)

driver.find_element(By.XPATH,"//input[@id='oneway']").click()
driver.find_element(By.XPATH,"//input[@id='roundtrip']").click()

from_city=driver.find_element(By.XPATH,"//label[text()='From City']").text
print(from_city)
driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys('Pune')

dest_city=driver.find_element(By.XPATH,"//label[text()='  Destination City']").text
print(dest_city)
driver.find_element(By.XPATH,"//input[@name='destcity']").send_keys('Nashik')

dept_date=driver.find_element(By.XPATH,"//label[text()='Departure Date']").text
print(dept_date)
driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys('06-02-2024')

return_date=driver.find_element(By.XPATH,"//label[text()='Return Date']").text
print(return_date)
driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys('07-02-2024')

del_opt=driver.find_element(By.XPATH,"//h2[text()='Delivery Option']").text
print(del_opt)

app_date=driver.find_element(By.XPATH,"//label[text()='Visa interview/ appointment date(optional)']").text
print(app_date)
driver.find_element(By.XPATH,"//input[@id='visadate']").send_keys('15-02-2024')

dummy_ticket=driver.find_element(By.XPATH,"//b[text()='How will you like to receive the dummy ticket(optional)']").text
print(dummy_ticket)

driver.find_element(By.XPATH,"//input[@id='eamil']").click()
email=driver.find_element(By.XPATH,"//span[text()='Email']").text
print(email)

driver.find_element(By.XPATH,"//input[@id='whatsapp']").click()
whatsapp=driver.find_element(By.XPATH,"//span[text()='WhatsApp']").text
print(whatsapp)

driver.find_element(By.XPATH,"//input[@id='female']").click()
both=driver.find_element(By.XPATH,"//span[text()='Both']").text
print(both)

billing_det=driver.find_element(By.XPATH,"//h2[text()='Billing Details']").text
print(billing_det)

billing_name=driver.find_element(By.XPATH,"//b[text()='Biling Name*']").text
print(billing_name)
driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys('Jay dev')

phone=driver.find_element(By.XPATH,"//b[text()='Phone*']").text
print(phone)
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys('1234567890')

email_add=driver.find_element(By.XPATH,"//b[text()='Email address*']").text
print(email_add)
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys('abc@gmail.com')

street_add=driver.find_element(By.XPATH,"(//b[text()='Street address*'])[1]").text
print(street_add)
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys('abc nashik')

country=driver.find_element(By.XPATH,"//b[text()='Country*']").text
print(country)
driver.find_element(By.XPATH,"//select[@id='billing_country']").send_keys('india')

postal=driver.find_element(By.XPATH,"//b[text()='Postcode / ZIP*']").text
print(postal)
driver.find_element(By.XPATH,"//input[@name='postcode']").send_keys('422216')

prefecture=driver.find_element(By.XPATH,"//b[text()='  Prefecture']").text
print(prefecture)
driver.find_element(By.XPATH,"//input[@name='prefecture']").send_keys('123')

street_address=driver.find_element(By.XPATH,"(//b[text()='Street address*'])[2]").text
print(street_address)
driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys('MG Road')
driver.find_element(By.XPATH,"//input[@id='street_address2']").send_keys('Kalika nagar')

most_visit=driver.find_element(By.XPATH,"//h2[text()='Most Visited Cities']").text
print(most_visit)

select_option=driver.find_element(By.XPATH,"//th[text()='Select Option']").text
print(select_option)
city_id=driver.find_element(By.XPATH,"//th[text()='City ID']").text
print(city_id)
city_name=driver.find_element(By.XPATH,"//th[text()='City Name']").text
print(city_name)
passengerss=driver.find_element(By.XPATH,"//th[text()='Passengers']").text
print(passengerss)

driver.find_element(By.XPATH,"(//input[@value='checkbox'])[1]").click()
driver.find_element(By.XPATH,"(//input[@value='checkbox'])[2]").click()
driver.find_element(By.XPATH,"(//input[@value='checkbox'])[3]").click()
driver.find_element(By.XPATH,"(//input[@value='checkbox'])[4]").click()
driver.find_element(By.XPATH,"(//input[@value='checkbox'])[5]").click()
driver.find_element(By.XPATH,"(//input[@value='checkbox'])[6]").click()
driver.find_element(By.XPATH,"(//input[@value='checkbox'])[7]").click()

contact_form=driver.find_element(By.XPATH,"(//h2[text()='Contact Form'])[1]").text
print(contact_form)
driver.find_element(By.XPATH,"(//input[@class='contact-form-name'])[1]").send_keys('Tushar')
driver.find_element(By.XPATH,"(//input[@class='contact-form-email'])[1]").send_keys("tushar@gmail.com")
driver.find_element(By.XPATH,"//textarea[@name='email-message']").send_keys('Passport help')
driver.find_element(By.XPATH,"(//input[@class='contact-form-button contact-form-button-submit'])[1]").click()

time.sleep(5)

driver.close()
