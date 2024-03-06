from selenium_base.selenium_code import SeleniumCode
from .dummy_website_page_data import *


class DummywebsitePage(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver)

    def dummy_options_tickets(self):
        self.click_element(dummy_options)