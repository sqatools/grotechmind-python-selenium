import time
import pytest
#from data import session_data import *
from modules.flight_booking_page import FlightBookingPage

@pytest.mark.usefixtures("launch_browser") #usefixtures
class Testflightbooking:

   def test_search_flight(self):
    self.fp=FlightBookingPage(self.driver)
    self.fp.enter_source_city("Mumbai")
    time.sleep(10)
