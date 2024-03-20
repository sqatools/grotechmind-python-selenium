import time
import pytest
from Modules.GroTechMind_Page import  GroTechMind_Flight_booking
from Data.Test_Data import *


@pytest.mark.usefixtures("launch_browser")
#1) Verify that users can successfully register for a new account.

class Test_flight_booking:

    @pytest.fixture(autouse=True)

    def setup(self):
        self.fb=GroTechMind_Flight_booking(self.driver)

    def test_click_login_button(self):
        #self.fb=GroTechMind_Flight_booking(self.driver)
        self.fb.clicklogin()
        time.sleep(5)

    def test_click_signup_button_to_user_registration(self):
        #self.fb=GroTechMind_Flight_booking(self.driver)
        self.fb.clicksign_up()
        time.sleep(5)

    def test_enter_login_details(self):
        #self.fb=GroTechMind_Flight_booking(self.driver)
        self.fb.enter_credential(email, username, password, repeat_pass)
        time.sleep(5)

    def test_click_check_box(self):
        #self.fb=GroTechMind_Flight_booking(self.driver)
        self.fb.click_check_box()
        time.sleep(5)

    def test_click_on_signup(self):
        #self.fb=GroTechMind_Flight_booking(self.driver)
        self.fb.click_on_signup()
        time.sleep(5)

# 2) Validate the login functionality with valid credentials.

    def test_click_on_sign_in_button(self):
        self.fb.click_on_sign_in1()
        time.sleep(4)

    def test_login_with_valid_credential(self):
        self.fb.enter_valid_credential(username, password)
        time.sleep(5)

    def test_login_valid_user(self):
        self.fb.click_on_Signin2()
        time.sleep(5)









