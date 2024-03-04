import pytest
import time
from modules.dummy_page import Dummy_Sqa
from data.test_data import *

# commands
"""
# command to run all test cases
python -m pytest -v .\tests\test_dummy.py --html-report=report.html

# command to run specific test case 
python -m pytest -v .\tests\test_dummy.py::TestDummyticketbooking::test_depart_return --html-report=report.html

# command to run test with markers.
python -m pytest -v -m smoke .\tests\test_dummy.py --html-report=report.html

"""

@pytest.mark.usefixtures("launch_browser") #confest launch_browser
class TestDummyticketbooking:

        @pytest.fixture(autouse=True)
        def setup(self):
            self.sqa = Dummy_Sqa(self.driver)

        def test_Dummy(self):
            self.sqa.dummy_radio()
            time.sleep(3)

        def test_passenger_info_input(self):
            #self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_passenger_details(f_name,l_name)

        @pytest.mark.smoke
        def test_birthday(self):
          #self.sqa=Dummy_Sqa(self.driver)
          self.sqa.enter_dob(dob_date)
          time.sleep(3)

        def test_passenger_sex(self):
            #self.sqa=Dummy_Sqa(self.driver)
            self.sqa.radio_button_element_sex()
            time.sleep(3)


        @pytest.mark.xpass
        def test_passenger_trip(self):
           #self.sqa=Dummy_Sqa(self.driver)
           self.sqa.radio_button_trip()



        @pytest.mark.xfail
        def test_passenger_city(self):
           #self.sqa=Dummy_Sqa(self.driver)
           self.sqa.enter_passenger_source_dest(s_city,d_city)
           #self.dw.enter_passenger_source_dest()
           time.sleep(3)


        @pytest.mark.skip(reason='this is unstable test case')
        def test_passenger_ticket(self):
         #self.sqa=Dummy_Sqa(self.driver)
         self.sqa.ticket_radio_button()
         time.sleep(3)

        def test_passenger_add(self):
          self.sqa=Dummy_Sqa(self.driver)
          self.sqa.passenger_billing_details(Bi_name,Bi_phone,
                                             Bi_email,Bi_street,
                                             Bi_street2,po_code,
                                             prefe,st_id)
          time.sleep(3)

        def test_passenger_visited_city(self):
          self.sqa=Dummy_Sqa(self.driver)
          self.sqa.passenger_visited_city_radio_button()
          time.sleep(3)


        def test_depart_return(self): #question for Sir
            #self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_depart_return(d_date,r_date)
            time.sleep(3)

        def test_enter_vdate(self):
            #self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_vdate(v_date)
            time.sleep(3)

        @pytest.mark.smoke2
        def test_enter_country_dd(self):
            #self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_country_dd(country_data)
            time.sleep(5)

        @pytest.mark.smoke2
        def test_add_more_passenger_dd(self):
            self.sqa.select_more_passenger(add_more_passenger)
            time.sleep(10)
