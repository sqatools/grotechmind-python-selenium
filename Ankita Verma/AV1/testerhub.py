from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/samplepagetest/")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='text' and @class='name']").send_keys("Anu")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Anu@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='url' and @id='g2599-website']").send_keys("Google.com")
time.sleep(1)
element=driver.find_element(By.ID,"g2599-experienceinyears").
drp=Select(element)
drp.select_by_visible_text("3-5")
#drp.select_by_value("7-10")
#drp.select_by_index(3)
driver.close()
