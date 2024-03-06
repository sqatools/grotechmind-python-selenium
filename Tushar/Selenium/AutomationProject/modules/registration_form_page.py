from selenium_base.selenium_code import seleniumcode
from .registration_form_page_data import *

class Regformpage(seleniumcode):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_email_password(self,email_id,password):
        self.fill_data(email,email_id) # def fill_data(self,locator,data):
        self.fill_data(pwd,password)

    def select_male_female_radio_button(self,person='female'):
        if person=='male':
            self.click_element(male_radio)
        else:
            self.click_element(female_radio)

    def select_skill_dropdown(self,value):
        self.click_element(select_skil_dd)
        dd_val_locator = (By.XPATH, f"//li[text()='{value}']")
        self.click_element(dd_val_locator)
