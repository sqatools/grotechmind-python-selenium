from selenium import webdriver
from selenium.webdriver.common.by import By
import time

d = webdriver.Chrome()
d.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
d.implicitly_wait(10)
d.maximize_window()
a = d.find_element(By.NAME,"globalSqa")
time.sleep(5)
d.switch_to.frame(a)
b = d.find_element(By.XPATH,"//div[@class='header_mail']").text
c = d.find_element(By.XPATH,"//div[@class='header_phone']").text
d.find_element(By.XPATH,"//div[@id='mobile_menu_toggler']").click()
print(b,c)
d.switch_to.default_content()
d.find_element(By.ID,"//div[@id='menu']//ul//a[text()='Contact Us']").click()
time.sleep(5)
d.close()
