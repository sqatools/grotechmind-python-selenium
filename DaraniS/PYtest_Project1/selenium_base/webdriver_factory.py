from selenium import webdriver
from data.session_data import timeout


class WebdriverFactory:
    def __init__(self, browser, url, timeout=timeout):
        self.url = url
        self.browser = browser
        self.timeout = timeout

    def get_driver_instance(self):
        if self.browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser.lower() == 'edge':
            driver = webdriver.Edge()

        driver.maximize_window()
        driver.implicitly_wait(self.timeout)
        driver.get(self.url)
        return driver
