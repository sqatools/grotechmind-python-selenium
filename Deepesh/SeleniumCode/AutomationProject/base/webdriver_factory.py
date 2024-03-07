from selenium import webdriver
from data import session_data as sd
from selenium.webdriver import ChromeOptions


class WebdriverFactory:
    def __init__(self, browser, url, timeout=sd.timeout, headless=sd.headless):
        self.url = url
        self.browser = browser
        self.timeout = timeout
        self.headless = headless

    def get_driver_instance(self):
        if self.browser.lower() == 'chrome':
            option = ChromeOptions()
            if self.headless:
                option.add_argument("--headless")
            driver = webdriver.Chrome(options=option)
        elif self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser.lower() == 'edge':
            driver = webdriver.Edge()

        driver.maximize_window()
        driver.implicitly_wait(self.timeout)
        driver.get(self.url)
        return driver
