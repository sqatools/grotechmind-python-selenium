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

    def enter_destination_city(self, city_name):
        self.fill_data(flight_to_field_input, city_name)

    def select_values_from_dropdown(self, city_name):
        city_selector = (By.XPATH, f"//span[contains(text(), '{city_name}')]//ancestor::li")
        self.click_element(city_selector)

    def select_src_dest_city(self, src_city_name, dest_city_name):
        self.enter_source_city(src_city_name)
        self.select_values_from_dropdown(src_city_name)
        self.enter_destination_city(dest_city_name)
        self.select_values_from_dropdown(dest_city_name)

    def select_departure_date(self, date):
        date_locator = (By.XPATH, f"//div[contains(@aria-label, '{date}')]")
        self.click_element(date_locator)
        self.click_element(date_picker_done_button)

    def select_number_of_adults(self, adult_num=1):
        for i in range(1, adult_num):
            self.click_element(adults_plus_icon)

    def select_number_of_child(self, child_num=0):
        for i in range(child_num):
            self.click_element(children_plus_icon)

    def select_number_of_infant(self, infant_num=0):
        for i in range(infant_num):
            self.click_element(infants_plus_icon)

    def select_travel_class(self, travel_class):
        travel_class = travel_class.lower()
        locator = (By.XPATH, f"//li[text()='{travel_class}']")
        self.click_element(locator)

    def travel_class_done_btn(self):
        self.click_element(travel_class_done_button)
