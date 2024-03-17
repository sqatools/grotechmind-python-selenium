from selenium_base.selenium_code import seleniumcode
from .dummy_ticket_booking_page_data import *

class Dummybookingticketpage(seleniumcode):
    def __init__(self,driver):
        #super(dummybookingticketpage, self).__init__(driver)
        super().__init__(driver)

    def radio_button_element(self):
        self.click_element(radio_button1)
        self.click_element(radio_button2)
        self.click_element(radio_button3)
        self.click_element(radio_button4)
        self.click_element(radio_button5)



    def enter_passenger_details(self,f_name,l_name):
        self.fill_data(first_name,f_name)
        self.fill_data(last_name,l_name)

    def enter_passenger_birth_date(self,date):
        self.click_element(Date_of_birth)
        self.fill_data(Date_of_birth,date)

    def radio_button_element_sex(self):
        self.click_element(male_radio)
        self.click_element(female_radio)

    # def enter_number_of_passenger(self,no_of_passenger):
    #    passenger_selector='passenger_dropdown'
    #    self.click_element(passenger_selector)


    def radio_button_trip(self):
        self.click_element(one_way_radio)
        self.click_element(round_radio)

    def enter_passenger_source_dest(self,s_city , d_city):
        self.fill_data(from_city, s_city)
        self.fill_data(dest_city, d_city)

    def enter_passenger_departure_return_date(self,date):
        self.click_element(departure_date)
        self.fill_data(departure_date,date)
        self.click_element(return_date)
        self.fill_data(return_date,date)

    def enter_passenger_visa_date(self,date):
        self.click_element(visa_date)
        self.fill_data(visa_date,date)



    def ticket_radio_button(self):
        self.click_element(email)
        self.click_element(whatapp)
        self.click_element(both)

    def passenger_billing_details(self,Bi_name,Bi_phone,Bi_email,Bi_street,po_code,prefe,st_id):
        self.fill_data(Billing_name,Bi_name)
        self.fill_data(Billing_phone,Bi_phone)
        self.fill_data(Billing_email,Bi_email)
        self.fill_data(Billing_street,Bi_street)
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









