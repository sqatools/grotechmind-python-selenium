from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.get_logger import logger, log_dir_path, dir_name
import os
log = logger


class SeleniumCode:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout=timeout)

    def get_element(self, locator: tuple):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            log.info(f"element found: {locator}")
            return element
        except Exception as e:
            snapshot_path = os.path.join(log_dir_path, f"element_{dir_name}.png")
            self.driver.save_screenshot(snapshot_path)
            log.info(f"Element not found: {locator}")
            log.info(f"{e}")
            return None

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()
        log.info(f"clicked on the element: {locator}")

    def fill_data(self, locator, data):
        element = self.get_element(locator)
        element.send_keys(data)
        log.info(f"enter {data} on the element: {locator}")
