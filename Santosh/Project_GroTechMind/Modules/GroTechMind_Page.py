from Selenium_Base.Selenium_Code import SeleniumCode
from .Page_Data import *


class GroTechMind_Flight_booking(SeleniumCode):

    def __init__(self,driver):
        super().__init__(driver)

    def clicklogin(self):
        self.click_elements(login_button)

    def clicksign_up(self):
        self.click_elements(sign_up)

    def enter_credential(self,email,username,password,repeat_pass):
        self.filled_data(enter_email_id,email)
        self.filled_data(user_name,username)
        self.filled_data(user_password,password)
        self.filled_data(repeat_user_password,repeat_pass)

    def click_check_box(self):
        self.click_elements(checkbox)

    def click_on_signup(self):
        self.click_elements(click_sign_up)








