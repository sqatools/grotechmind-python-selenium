from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("prefs" , True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.goibibo.com/")

