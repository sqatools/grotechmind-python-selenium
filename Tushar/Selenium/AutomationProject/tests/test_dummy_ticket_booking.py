import time
import pytest
from  modules.dummy_ticket_booking_page import Dummybookingticketpage
from data.test_data import *

@pytest.mark.usefixtures("launch_browser")
class TestDummyticketbooking:

     def test_radio_button(self):
        self.dw=Dummybookingticketpage(self.driver)
        self.dw.radio_button_element()

     def test_passenger_info_input(self):
        self.dw=Dummybookingticketpage(self.driver)
        self.dw.enter_passenger_details(f_name,l_name)

     def test_passenger_sex(self):
        self.dw=Dummybookingticketpage(self.driver)
        self.dw.radio_button_element_sex()

        time.sleep(10)

     def test_passenger_trip(self):
        self.dw=Dummybookingticketpage(self.driver)
        self.dw.radio_button_trip()



     def test_passenger_city(self):
         self.dw=Dummybookingticketpage(self.driver)
         self.dw.enter_passenger_source_dest(s_city,d_city)
         #self.dw.enter_passenger_source_dest()

         time.sleep(10)


     def test_passenger_ticket(self):
         self.dw=Dummybookingticketpage(self.driver)
         self.dw.ticket_radio_button()


         time.sleep(10)

     def test_passenger_add(self):
         self.dw=Dummybookingticketpage(self.driver)
         self.dw.passenger_billing_details(Bi_name,Bi_phone,Bi_email,Bi_street,po_code,prefe,st_id)

         time.sleep(10)

     def test_passenger_visited_city(self):
         self.dw=Dummybookingticketpage(self.driver)
         self.dw.passenger_visited_city_radio_button()


         time.sleep(10)









