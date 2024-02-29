import time
import pytest
from modules.flight_booking_page import FlightBookingPage
from data.test_data import *

from data.test_data import src_city_name


@pytest.mark.usefixtures("launch_browser")
class TestFlightBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fp = FlightBookingPage(self.driver)

    def test_search_flight(self):
        self.fp.close_mobile_popup()
        self.fp.select_src_dest_city(src_city_name, dest_city_name)
        self.fp.select_departure_date(depart_data)

    def test_select_travel_class(self):
        self.fp.select_number_of_adults(2)
        self.fp.select_number_of_child(1)
        self.fp.select_number_of_infant(1)
        self.fp.select_travel_class(travel_class)
        time.sleep(10)
        self.fp.travel_class_done_btn()

