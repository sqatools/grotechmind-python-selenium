import time
import pytest
from modules.flight_booking_page import flightbookingpage


@pytest.mark.usefixtures("launch_browser")
class testflightbooking:

    def test_search_flight(self):
        self.fp=flightbookingpage(self.driver)
        self.fp.enter_source_city("Mumbai")
        time.sleep(10)

