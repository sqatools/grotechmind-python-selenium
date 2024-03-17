from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumCode:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,timeout=30)

    def get_element(self,locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()

    def fill_data(self,locator,input_data):
        element = self.get_element(locator)
        element.send_key(input_data)


















