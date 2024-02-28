from selenium_base.selenium_code import seleniumcode
from .flight_booking_page_data import *

class flightbookingpage(seleniumcode):
    def __init__(self,driver):
        super().__init__(driver)


    def enter_source_city(self,city_name):
        self.element_click(flight_from_field)
        self.fill_data(flight_from_field_input,data)
