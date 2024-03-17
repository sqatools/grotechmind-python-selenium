import time
import pytest
from Modules.GroTechMind_Page import  GroTechMind_Flight_booking
from Data.Test_Data import *


@pytest.mark.usefixtures("launch_browser")

class Test_flight_booking:

    @pytest.fixture(autouse=True)

    def setup(self):
        self.fb=GroTechMind_Flight_booking(self.driver)

    def test_login(self):
        #self.fb=GroTechMind_Flight_booking(self.driver)
        self.fb.clicklogin()
        time.sleep(5)

    def test_signup(self):
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









