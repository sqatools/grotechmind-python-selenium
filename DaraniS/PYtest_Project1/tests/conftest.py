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


@pytest.fixture(scope='class')
def amazom_broswer(request):
    wb = WebdriverFactory(browser=browser, url=website_url_amazon)
    driver = wb.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope='class')
def dummy_broswer(request):
    wb = WebdriverFactory(browser=browser, url=website_dummy_url)
    driver = wb.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope='class')
def gtm_broswer(request):
    wb = WebdriverFactory(browser=browser, url=website_gtm_url)
    driver = wb.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()