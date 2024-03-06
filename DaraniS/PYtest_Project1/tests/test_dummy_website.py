import time
import pytest
from modules.dummy_website_page import DummywebsitePage
from data.test_data import *

from data.test_data import src_city_name


@pytest.mark.usefixtures("dummy_broswer")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fp = DummywebsitePage(self.driver)

    def test_dummy_options(self):
        self.fp.dummy_options_tickets()
        time.sleep(20)
