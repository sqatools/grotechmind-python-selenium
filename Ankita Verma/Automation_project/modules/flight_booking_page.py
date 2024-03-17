from selenium_base.selenium_code import SeleniumCode #parentclass
from .flight_booking_page_data import *

class FlightBookingPage(SeleniumCode):# importing the page class into test class
    def __init__(self,driver):
       super().__init__(driver)

    def close_mobile_popup(self):
        self.click_element(mobile_login_popup)

    def enter_source_city(self, city_name):
        self.click_element(source_city_field)
        self.fill_data(source_city_field_input,city_name)

    def enter_destination_city(self,city_name ):
         self.click_element(destination_city_field)
         self.fill_data(destination_city_field,city_name)
