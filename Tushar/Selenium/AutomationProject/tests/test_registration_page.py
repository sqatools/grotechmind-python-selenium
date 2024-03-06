import time
import pytest
from modules.registration_form_page import Regformpage

from data.test_data import *

@pytest.mark.usefixtures("launch_browser")
class Testregistrationpage:

    @pytest.fixture(autouse=True)
    def setup(self):
            self.rp = Regformpage(self.driver)

    def test_email_password(self):
        self.rp.enter_email_password(email_id,password)

        time.sleep(5)


    def test_radio_male_female(self):
        self.rp.select_male_female_radio_button()


    def test_enter_skill_dd(self):
        self.rp.select_skill_dropdown(t_value)



        time.sleep(5)




