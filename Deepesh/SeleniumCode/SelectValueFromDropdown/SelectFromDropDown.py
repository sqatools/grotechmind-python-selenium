from selenium import webdriver
#from selenium.webdriver.common.by import By as india
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.implicitly_wait(10)
#driver.find_element(india.ID, "fistname").send_keys("tushar")

pass_dropdown = driver.find_element(By.ID, "admorepass")
select_obj = Select(pass_dropdown)
# select_obj.select_by_index(1) # select by index

# select by visible text
# select_obj.select_by_visible_text("Add 3 more passenger (200%)")

# Select by value
select_obj.select_by_value("3")
time.sleep(5)
# Select country from dropdown

country_dropdwn = driver.find_element(By.ID, "billing_country")
select_country = Select(country_dropdwn)
select_country.select_by_visible_text("India")
time.sleep(5)

driver.close()
