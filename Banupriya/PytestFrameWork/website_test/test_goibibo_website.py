
import pytest
from selenium.webdriver.common.by import By
from ..test_datafile import *
import time
def test_goibibo_website(browser):
    browser.get(website_url)
    

    time.sleep(5)-