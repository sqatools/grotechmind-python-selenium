from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.booking.com/index.en.html?aid=393655&label=msn-TF7fYzyNdGSbuXzNJiosWA-79852067815503:tikwd-16681414380:loc-90:neo:mte:lp156924:dec:qsgoibibo&utm_campaign=English%20EN%20ROW-CAUS&utm_medium=cpc&utm_source=bing&utm_term=TF7fYzyNdGSbuXzNJiosWA&msclkid=79a2b75fbb491aefdb52d2e4d1f427bb")
driver.find_element(By.XPATH,"//input[@name='ss']").send_keys("Mumbai")

time.sleep(5)

driver.close()
