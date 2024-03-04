import pytest
import time
from modules.dummy_page import Dummy_Sqa
from data.test_data import *
@pytest.mark.usefixtures("launch_browser") #confest launch_browser
class TestDummyticketbooking:
        def test_Dummy(self):
            self.sqa=Dummy_Sqa(self.driver)
            self.sqa.dummy_radio()
            time.sleep(10)

        def test_passenger_info_input(self):
            self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_passenger_details(f_name,l_name)

        def test_birthday(self):
          self.sqa=Dummy_Sqa(self.driver)
          self.sqa.enter_dob(dob_date)
          time.sleep(10)

        def test_passenger_sex(self):
            self.sqa=Dummy_Sqa(self.driver)
            self.sqa.radio_button_element_sex()
            time.sleep(10)

        def test_passenger_trip(self):
           self.sqa=Dummy_Sqa(self.driver)
           self.sqa.radio_button_trip()



        def test_passenger_city(self):
           self.sqa=Dummy_Sqa(self.driver)
           self.sqa.enter_passenger_source_dest(s_city,d_city)
           #self.dw.enter_passenger_source_dest()
           time.sleep(10)


        def test_passenger_ticket(self):
         self.sqa=Dummy_Sqa(self.driver)
         self.sqa.ticket_radio_button()
         time.sleep(10)

        def test_passenger_add(self):
          self.sqa=Dummy_Sqa(self.driver)
          self.sqa.passenger_billing_details(Bi_name,Bi_phone,Bi_email,Bi_street,Bi_street2,po_code,prefe,st_id)
          time.sleep(10)

        def test_passenger_visited_city(self):
          self.sqa=Dummy_Sqa(self.driver)
          self.sqa.passenger_visited_city_radio_button()
          time.sleep(10)


        def test_depart_return(self): #question for Sir
            self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_depart_return(d_date,r_date)
            time.sleep(10)

        def test_enter_vdate(self):
            self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_vdate(v_date)
            time.sleep(10)

        """def test_enter_country_dd(self):
            self.sqa=Dummy_Sqa(self.driver)
            self.sqa.enter_country_dd()
            time.sleep(10)"""

