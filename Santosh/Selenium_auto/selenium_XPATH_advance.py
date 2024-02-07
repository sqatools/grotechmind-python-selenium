''''
    # Advance Methods in XPATH

    1) Following:
                //tagname[@attrib='value']//following::tagname[@attribute='value']
                //input[@value='radio_345']//following::input[@id='male']
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

#driver.find_element(By.XPATH,"//input[@value='radio_123' and @type='radio']").click()
#driver.find_element(By.XPATH,"//input[@value='radio_345']//following::input[@id='male']").click()

#driver.find_element(By.XPATH,"//h2[text()='Passenger Details']//following::input[@id='male']").click()
# var=driver.find_element(By.XPATH,"//input[@value='radio_558']//following::h2[text()='Passenger Details']").text
# print(var)


time.sleep(5)

driver.close()

