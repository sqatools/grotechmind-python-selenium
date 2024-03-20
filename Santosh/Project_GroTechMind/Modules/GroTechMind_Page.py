from Selenium_Base.Selenium_Code import SeleniumCode
from .Page_Data import *


class GroTechMind_Flight_booking(SeleniumCode):

    def __init__(self,driver):
        super().__init__(driver)
#1) Verify that users can successfully register for a new account.
    def clicklogin(self):
        self.click_elements(login_button)

    def clicksign_up(self):
        self.click_elements(sign_up)

    def enter_credential(self,email,username,password,repeat_pass):
        self.filled_data(enter_email_id,email) # locator=enter_email_id and email=Test data
        self.filled_data(user_name,username)
        self.filled_data(user_password,password)
        self.filled_data(repeat_user_password,repeat_pass)

    def click_check_box(self):
        self.click_elements(checkbox)

    def click_on_signup(self):
        self.click_elements(click_sign_up)

#2) Validate the login functionality with valid credentials.

    def click_on_sign_in1(self):
        self.click_elements(click_to_login)

    def enter_valid_credential(self,username,password):
        self.filled_data(valid_user_name,username) # locator=valid_user_name and username=Test data
        self.filled_data(valid_password,password)

    def click_on_Signin2(self):
        self.click_elements(final_click_sing_in)







