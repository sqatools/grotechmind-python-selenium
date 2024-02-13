from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH,"//span[text()='Grocery']").click()
driver.find_element(By.XPATH,"(//img[@alt='Flipkart'])[2]").click()

#driver.find_element(By.XPATH,"//span[text()='Mobiles']").click()
#driver.find_element(By.XPATH,"//img[@title='Flipkart' and @alt='Flipkart']").click()

# driver.find_element(By.XPATH,"//img[@alt='Fashion']").click()
# time.sleep(10)
# driver.find_element(By.XPATH,"//picture[@title='Flipkart']//following::img[@title='Flipkart']").click()
#
# driver.find_element(By.XPATH,"//img[@alt='Electronics']").click()
# driver.find_element(By.XPATH,"(//img[@alt='Flipkart'])[2]").click()
#
# driver.find_element(By.XPATH,"//img[@alt='Home & Furniture']").click()
# driver.find_element(By.XPATH,"(//img[@alt='Flipkart'])[2]").click()

driver.find_element(By.XPATH,"//span[text()='Appliances']").click()
driver.find_element(By.XPATH,"//img[@alt='Flipkart']").click()

driver.find_element(By.XPATH,"//span[text()='Travel']").click()
driver.find_element(By.XPATH,"//picture[@title='Flipkart']//following::img[@title='Flipkart']").click()

driver.find_element(By.XPATH,"//img[@alt='Beauty, Toys & More']").click()
driver.find_element(By.XPATH,"//picture[@title='Flipkart']//following::img[@title='Flipkart']").click()














time.sleep(5)
driver.close()
