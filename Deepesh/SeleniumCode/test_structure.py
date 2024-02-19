from selenium import  webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)

def login(username, password):
    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    assert "login successful"

def registration(param):
    """All registrations fields"""
    pass

def groups(params):
    """All group related field"""


# login()
# registration()
# groups()