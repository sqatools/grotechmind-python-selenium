from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login.php")
driver.find_element(By.ID,"email").send_keys("santoshWwadikar77@gmail.com")
driver.find_element(By.ID,"pass").send_keys("AcebwA@9900")
driver.find_element(By.NAME,"login").click
time.sleep(10)
#driver.close()
