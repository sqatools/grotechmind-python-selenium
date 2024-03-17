from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumCode:
    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.Wait=WebDriverWait(self.driver,timeout)

    def get_elements(self,locator):
        element=self.Wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_elements(self,locator):
        element=self.get_elements(locator)
        element.click()

    def filled_data(self,locator,data):
        element = self.get_elements(locator)
        element.send_keys(data)

    def select_Dropdown(self,locator,value):
        element = self.get_elements(locator)
        obj = Select(element)
        obj.select_by_value(value)
