from selenium_base.selenium_code import SeleniumCode
from flight_booking_page_data import *

class FlightBookingPage(SeleniumCode):

    def __init__(self,driver):
        super().__init__(driver)

    def enter_source_city(self, city_name):
        self.click_element(source_city_field)
        self.fill_data(source_city_field_input,city_name)
