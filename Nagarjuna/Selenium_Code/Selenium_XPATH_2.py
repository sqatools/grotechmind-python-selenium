from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options= options)

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")
time.sleep(1)






""""
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element(By.XPATH,"(//textarea[@name='q'])").send_keys("Goibibo")
time.sleep(1)
driver.find_element(By.XPATH,"(//input[@value='Google Search'][1])").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//div[contains(text(),'Book Flights Hotels on GoIbibo - Daily Steal Deal on Flights')])").click()
# driver.find_element(By.XPATH,"(//div[@class='GKS7s']//following::div[contains(text(),'goibibo.com')][1])").click()

#time.sleep(1)
"""






