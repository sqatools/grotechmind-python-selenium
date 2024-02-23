import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from test_data import *



def test_one_way(browser):
    browser.get(url)
    browser.find_element(By.XPATH, "//p[text()='One-way']").click()
    browser.find_element(By.XPATH, "(//p[text()='Enter city or airport'])[1]").click()
    time.sleep(5)


def test_two_way(browser):
    browser.get(url)
    browser.find_element(By.XPATH, "//p[text()='Round-trip']").click()
    browser.find_element(By.XPATH, "(//p[text()='Enter city or airport'])[1]").click()
    time.sleep(5)


def test_multiple_way(browser):
    browser.get(url)
    browser.find_element(By.XPATH, "//p[text()='Multi-city']").click()
    browser.find_element(By.XPATH, "(//p[text()='Enter city or airport'])[1]").click()
    time.sleep(5)
