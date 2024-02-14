import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

driver.find_element(By.LINK_TEXT, "What is Manual Testing").click()
time.sleep(5)
browser_windows = driver.window_handles
print("total number of windows :", browser_windows)
driver.switch_to.window(browser_windows[1])

driver.find_element(By.NAME, "q").send_keys("Python Programming")
driver.find_element(By.XPATH, "//input[@value='Search']").click()
time.sleep(5)

driver.close()

driver.switch_to.window(browser_windows[0])
time.sleep(5)
driver.find_element(By.XPATH, "//li//a[text()='Home']").click()

time.sleep(5)
driver.close()


