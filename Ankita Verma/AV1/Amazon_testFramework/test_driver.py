import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close the browser
    driver.quit()

def test_login(browser):
    # Navigate to the login page
    browser.get('https://www.saucedemo.com/')

    # Perform actions - fill in username and password
    browser.find_element_by_id('username').send_keys('standard_user')
    browser.find_element_by_id('password').send_keys('secret_sauce')
    browser.find_element_by_id('login-btn').click()

    # Assert - check for successful login
    assert 'Welcome, testuser!' in browser.page_source
