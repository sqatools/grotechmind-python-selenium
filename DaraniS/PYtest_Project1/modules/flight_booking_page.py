from selenium_base.selenium_code import SeleniumCode
from .flight_booking_page_data import *


class FlightBookingPage(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver)

    def oneway_click(self):
        self.click_element(one_click_path)