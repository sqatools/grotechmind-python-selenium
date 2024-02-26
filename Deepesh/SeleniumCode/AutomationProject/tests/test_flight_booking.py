import time

import pytest
from modules.flight_booking_page import FlightBookingPage


@pytest.mark.usefixtures("launch_browser")
class TestFlightBooking:

    def test_search_flight(self):
        self.fp = FlightBookingPage(self.driver)
        self.fp.close_mobile_popup()
        self.fp.enter_source_city("Mumbai")
        time.sleep(10)