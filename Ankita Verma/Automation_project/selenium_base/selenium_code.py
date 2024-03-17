from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
class SeleniumCode:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,timeout=30)

    def  get_element(self,locator):# wait untill element found
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self,locator):#click element
        element = self.get_element(locator)
        element.click()

    def fill_data(self,locator,input_data):
        element = self.get_element(locator)
        element.send_keys(input_data)

    def select_value_from_dropdown(self, locator, value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)

