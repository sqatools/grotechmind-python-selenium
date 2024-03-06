import time

from selenium_base.selenium_code import SeleniumCode
from .grow_tech_minds_reg_page import *


class GrowTMReg(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver)

    def read_reg(self):
        time.sleep(10)
        self.click_element(read_only_reg)

    def reg_fill(self,input_email,input_password):
        self.fill_data(reg_email,input_email)
        self.fill_data(reg_password,input_password)
        self.click_element(reg_female)
        self.click_element(reg_skills)
        self.click_element(reg_skills_drop)
