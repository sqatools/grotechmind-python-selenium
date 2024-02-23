import pytest
import logging
from selenium.webdriver.common.by import By
from ..test_data import *
import time
from .log_config import logger

log = logger

def test_search_on_google(browser):
    browser.get(website_url)
    log.info(f"launching url : {website_url}")
    browser.find_element(By.NAME, "q").send_keys("Python Programming")
    log.info(f"sending data to search: Python Programming")
    browser.find_element(By.NAME, "btnK").click()
    log.info(f"click on google seach button : locator : btnK")


def test_python_website(browser):
    browser.find_element(By.LINK_TEXT, "Python For Beginners").click()
    logger.info("Search for Python for Beginners website")
    browser.find_element(By.LINK_TEXT, "Downloads").click()
    logger.info("Navigate to download section")
    browser.find_element(By.LINK_TEXT, "Download Python 3.12.2").click()
    logger.info("Click on latest python installer")
    time.sleep(5)
