import time
import pytest
from modules.flight_booking_page import flightbookingpage


@pytest.mark.usefixtures("launch_browser")
class Testflightbooking:




    def test_search_flight(self):
        self.fp=flightbookingpage(self.driver)
        self.fp.close_mobile_popup()
        self.fp.enter_source_city("Mumbai")
        time.sleep(10)

