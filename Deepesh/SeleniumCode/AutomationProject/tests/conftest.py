import pytest
from data.session_data import *
from selenium_base.webdriver_factory import WebdriverFactory


@pytest.fixture(scope='class')
def launch_browser(request):
    wb = WebdriverFactory(browser=browser, url=website_url)
    driver = wb.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()

