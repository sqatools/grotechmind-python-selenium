import time

from selenium_base.selenium_code import SeleniumCode
from .dummy_page_data import *
from data .test_data import *
from selenium.webdriver.support.select import Select
class Dummy_Sqa(SeleniumCode): #selenium_code file class copied here
    def __init__(self,driver):
       super().__init__(driver)

    def dummy_radio(self):
        self.click_element(radio_button1)
        self.click_element(radio_button2)
        self.click_element(radio_button3)
        self.click_element(radio_button4)
        self.click_element(radio_button5)


    def user_info(self,first_name,last_name):
            self.fill_data(first_name)
            self.fill_data(last_name)

    def enter_passenger_details(self,f_name,l_name):
        #self.click_element(first_name)
        self.fill_data(first_name,f_name)
        #self.click_element(last_name)
        self.fill_data(last_name,l_name)

    def radio_button_element_sex(self):
        self.click_element(male_radio)
        self.click_element(female_radio)

    def radio_button_trip(self):
        self.click_element(one_way_radio)
        self.click_element(round_radio)

    def enter_passenger_source_dest(self,s_city , d_city):
        self.fill_data(from_city, s_city)
        self.fill_data(dest_city, d_city)


    def ticket_radio_button(self):
        self.click_element(email)
        self.click_element(whatapp)
        self.click_element(both)

    def passenger_billing_details(self,Bi_name,Bi_phone,Bi_email,Bi_street,Bi_street2,po_code,prefe,st_id):
        self.fill_data(Billing_name,Bi_name)
        self.fill_data(Billing_phone,Bi_phone)
        self.fill_data(Billing_email,Bi_email)
        self.fill_data(Billing_street,Bi_street)
        self.fill_data(Billing_street2,Bi_street2)
        self.fill_data(post_code,po_code)
        self.fill_data(prefecture,prefe)
        self.fill_data(street_id,st_id)

    def passenger_visited_city_radio_button(self):
        self.click_element(city_radio_button1)
        self.click_element(city_radio_button2)
        self.click_element(city_radio_button3)
        self.click_element(city_radio_button4)
        self.click_element(city_radio_button5)
        self.click_element(city_radio_button6)
        self.click_element(city_radio_button7)

    def enter_dob(self,date):
        self.click_element(dob)
        self.fill_data(dob,date)

    def enter_depart_return(self,d_date,r_date):
        self.click_element(depart_date)
        self.fill_data(depart_date,d_date)
        self.click_element(return_date)
        self.fill_data(return_date,r_date)

    def enter_vdate(self,date):
        self.click_element(visa_date)
        self.fill_data(visa_date,date)

    """def enter_country_dd(self):
        self.select_object=Select(country_path)
        #self.select_by_visible_text('country_data')
        #select.select_by_value(country_path,'india')
        self.click_element(country_data)"""

