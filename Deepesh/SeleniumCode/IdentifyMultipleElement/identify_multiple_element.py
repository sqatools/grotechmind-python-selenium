from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
element_list = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print("Total number of element :", len(element_list))
for elem in element_list:
    time.sleep(1)
    elem.click()

citys_elements = driver.find_elements(By.XPATH, "//table[@id='cities']//tr/td[3]")
for i in range(2):
    print(citys_elements[i].text)
time.sleep(5)
driver.close()
