import time
import pytest
from modules.amazon_signin import AmazonPagedata
from data.test_data import *




@pytest.mark.usefixtures("amazom_broswer")
class TestAmazonPage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fp = AmazonPagedata(self.driver)



    def test_search_amazon(self):
        self.fp.amazon_sigh_popup()
        self.fp.amazon_create_account()


    def test_create_amazon(self):
        self.fp.amazon_enter_email(num_data)
        self.fp.amazon_continue()
        time.sleep(30)



