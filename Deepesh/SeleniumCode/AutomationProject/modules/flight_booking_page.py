from selenium_base.selenium_code import SeleniumCode
from .flight_booking_page_data import *

class FlightBookingPage(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver)

    def close_mobile_popup(self):
        self.click_element(mobile_login_popup)

    def enter_source_city(self, city_name):
        self.click_element(flight_from_field)
        self.fill_data(flight_from_field_input, city_name)