import time
import pytest
from data import session_data import *

@pytest.mark.usefixtures("launch_browser") #usefixtures
class Testfilghtbooking

   def test_search_flight(self):
    self.fp=Testfilghtbooking(self.driver)
    self.fp.enter_source_city("Mumbai")
    time.sleep(10)
