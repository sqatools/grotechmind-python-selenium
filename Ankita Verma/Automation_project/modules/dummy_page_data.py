from selenium.webdriver.common.by import By

radio_button1 = (By.XPATH, "//input[@value='radio_123']")
radio_button2 = (By.XPATH, "//input[@value='radio_345']")
radio_button3 = (By.XPATH, "//input[@value='radio_678']")
radio_button4 = (By.XPATH, "(//input[@value='radio_558'])[1]")
radio_button5 = (By.XPATH, "(//input[@value='radio_558'])[2]")

first_name = (By.XPATH, "(//input[@id='firstname'])[1]")
last_name = (By.XPATH, "(//input[@id='firstname'])[2]")
birthday = (By.XPATH, "//input[@id='birthday']")
male_radio = (By.XPATH, "//input[@id='male']")
female_radio = (By.XPATH, "(//input[@id='female'])[1]")
one_way_radio = (By.XPATH, "//input[@id='oneway']")
round_radio = (By.XPATH, "//input[@id='roundtrip']")
from_city = (By.ID, "fromcity")
dest_city = (By.ID, "destcity")
email = (By.XPATH, "//input[@id='eamil']")
whatapp = (By.XPATH, "//input[@id='whatsapp']")
both = (By.XPATH, "(//input[@id='female'])[2]")
Billing_name = (By.XPATH, "//input[@id='billing_name']")
Billing_phone = (By.XPATH, "//input[@id='billing_phone']")
Billing_email = (By.XPATH, "//input[@id='billing_email']")
Billing_street = (By.XPATH, "//input[@id='billing_address']")
Billing_street2 = (By.XPATH, "//input[@id='street_address2']")
post_code = (By.XPATH, "//input[@id='postcode']")
prefecture = (By.XPATH, "//input[@id='Prefecture']")
street_id = (By.XPATH, "//input[@id='street_address1']")
city_radio_button1 = (By.XPATH, "(//input[@value='checkbox'])[1]")
city_radio_button2 = (By.XPATH, "(//input[@value='checkbox'])[2]")
city_radio_button3 = (By.XPATH, "(//input[@value='checkbox'])[3]")
city_radio_button4 = (By.XPATH, "(//input[@value='checkbox'])[4]")
city_radio_button5 = (By.XPATH, "(//input[@value='checkbox'])[5]")
city_radio_button6 = (By.XPATH, "(//input[@value='checkbox'])[6]")
city_radio_button7 = (By.XPATH, "(//input[@value='checkbox'])[7]")
dob = (By.XPATH, "//input[@id='birthday']")
depart_date = (By.XPATH, "//input[@id='departdate']")
return_date = (By.XPATH, "//input[@id='returndate']")
visa_date = (By.XPATH, "//input[@id='visadate']")
country_path = (By.XPATH, "//select[@id='billing_country']")
add_more_pass_element = (By.ID, "admorepass")