import time
import pytest
from modules.grow_tech_minds_reg import GrowTMReg
from data.test_data import *







@pytest.mark.usefixtures("gtm_broswer")
class TestGTMWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fp = GrowTMReg(self.driver)

    def test_gmt_reg(self):
        self.fp.read_reg()


    def test_reg_fill(self):
        self.fp.reg_fill(input_email,input_password)

        time.sleep(5)


