import time
from typing import Type

import pytest
#from data import session_data import *
from modules.flight_booking_page import FlightBookingPage #creating object of the class

@pytest.mark.usefixtures("launch_browser") #usefixtures
class Testflightbooking:

   def test_search_flight(self):
    self.fp=FlightBookingPage(self.driver)
    self.fp.close_mobile_popup()
    self.fp.enter_source_city("Mumbai") # what is fp ??? object of the class
    self.fp.enter_destination_city("Delhi")
    time.sleep(10)


