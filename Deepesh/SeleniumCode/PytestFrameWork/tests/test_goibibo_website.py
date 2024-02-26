import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("launch_browser")
class TestGoibibo:

    def test_search_flight(self):

        self.driver.get("https://www.goibibo.com/")
        element = self.driver.find_element(By.XPATH, "//span[@class='logSprite icClose']")
        if element.is_displayed():
            element.click()

        self.driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::p").click()
        self.driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::input").send_keys("Mumbai")
        time.sleep(5)
