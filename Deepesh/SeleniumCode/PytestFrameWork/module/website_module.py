from test_data.test_data import *
from utilities.log_config import get_logger
from selenium.webdriver.common.by import By

log = get_logger()

def search_on_google(driver):
    driver.get(website_url)
    log.info(f"launching url : {website_url}")
    driver.find_element(By.NAME, "q").send_keys("Python Programming")
    log.info(f"sending data to search: Python Programming")
    driver.find_element(By.NAME, "btnK").click()
    log.info(f"click on google seach button : locator : btnK")