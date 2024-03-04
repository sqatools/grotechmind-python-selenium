from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class seleniumcode:
    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(self.driver,timeout)

    def get_element(self,locator:tuple):
        element=self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()

    def fill_data(self,locator,data):
        element = self.get_element(locator)
        element.send_keys(data)

    def select_dropdown(self,locator):
        element=self.get_element(locator)
        element.click()

        self.select_obj=select(passenger_dropdown)
        self.select_obj.select_by_index(1)

