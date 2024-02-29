import time
import pytest
from modules.flight_booking_page import FlightBookingPage
from ..data.test_data import *

# from data.test_data import src_city_name


@pytest.mark.usefixtures("launch_browser")
class TestFlightBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fp = FlightBookingPage(self.driver)

    def test_search_flight(self):
        self.fp.oneway_click()