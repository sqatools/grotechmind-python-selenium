from selenium_base.selenium_code import SeleniumCode
from .amazon_signin_data import *

class AmazonPagedata(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver)

    def amazon_sigh_popup(self):
        self.click_element(amazon_start_here)

    def amazon_create_account(self):
        self.click_element(amazon_create_account)

    def amazon_enter_email(self,num_data):
        self.click_element(amazon_enter_email)
        self.fill_data(amazon_enter_email,num_data)

    def amazon_continue(self):
        self.click_element(amazon_click_continue)



