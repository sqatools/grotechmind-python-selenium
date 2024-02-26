import pytest
import logging
import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from selenium.webdriver.common.by import By
from test_data.test_data import *
import time
#from utilities.get_logger import logger
from utilities.log_config import get_logger
from module.website_module import search_on_google

log = get_logger()

def test_search_on_google(browser):
    search_on_google(browser)


def test_python_website(browser):
    browser.find_element(By.LINK_TEXT, "Python For Beginners").click()
    log.info("Search for Python for Beginners website")
    browser.find_element(By.LINK_TEXT, "Downloads").click()
    log.info("Navigate to download section")
    browser.find_element(By.LINK_TEXT, "Download Python 3.12.2").click()
    log.info("Click on latest python installer")
    time.sleep(5)
