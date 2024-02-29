import pytest
from selenium.webdriver.common.by import By
from ..test_data import *
import time

def test_flight_booking(browser):
    browser.get(website_url)
    browser.find_element(By.XPATH,"//span[contains(text(),'Flights')]").click
    browser.find_element(By.XPATH,"//div//span[contains(text(),'From')][1]").send_keys("Hyderabad")
    browser.find_element(By.XPATH,"//div//span[contains(text(),'To')]").send_keys("Mumbai")
    browser.find_element(By.XPATH,"//span[contains(text(),'SEARCH FLIGHTS')]").click()
    time.sleep(5)

def test_hotel_booking(browser):
    browser.get(website_url)
    browser.find_element(By.XPATH,"//span[contains(text(),'Hotels')]").click()
    browser.find_element(By.XPATH,"//input[@data-testid='home-autosuggest-input']").send_keys("Bangalore")
    browser.find_element(By.XPATH,"//button[@data-testid='searchHotelBtn']").click()

    time.sleep(5)
