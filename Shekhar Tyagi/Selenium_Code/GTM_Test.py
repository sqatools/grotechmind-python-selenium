from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@value='radio_558'])[1]").click()
time.sleep(1)

driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]").send_keys("Shekhar")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]").send_keys("Tyagi")
time.sleep(1)

driver.find_element(By.ID,"birthday").send_keys("10/07/1996")
time.sleep(1)

driver.find_element(By.ID, "male").click()
time.sleep(1)

drop = driver.find_element(By.ID,"admorepass")
select = Select(drop)
select.select_by_value('3')
time.sleep(2)

driver.find_element(By.ID,"oneway").click()
time.sleep(1)

driver.find_element(By.ID,"fromcity").send_keys("New Delhi")
time.sleep(1)
driver.find_element(By.ID,"destcity").send_keys("Bangalore")
time.sleep(1)

driver.find_element(By.ID,"departdate").send_keys("02/02/2024")
time.sleep(1)
driver.find_element(By.ID,"returndate").send_keys("02/10/2024")
time.sleep(1)

driver.find_element(By.ID,"visadate").send_keys("02/05/2024")
time.sleep(1)

driver.find_element(By.XPATH, "//div[9]//input[3]").click()
time.sleep(1)

driver.find_element(By.ID,"billing_name").send_keys("Western Boy")
time.sleep(1)

driver.find_element(By.ID,"billing_phone").send_keys("9760939256")
time.sleep(1)

driver.find_element(By.ID,"billing_email").send_keys("Shekhartyagi53@gmail.com")
time.sleep(1)

driver.find_element(By.ID,"billing_address").send_keys("H/s No 18, CP, New Delhi, 110011")
time.sleep(1)

driver.find_element(By.XPATH,"//option[@vlaue='IN']").click()
time.sleep(1)
driver.find_element(By.ID,"postcode").send_keys("110011")
time.sleep(1)
driver.find_element(By.ID,"Prefecture").send_keys("N/A")
time.sleep(1)

driver.find_element(By.ID,"street_address1").send_keys("H/s No 18, Road no-NH-24, Connaught Place, New Delhi")
time.sleep(1)

driver.find_element(By.ID,"street_address2").send_keys("Near India Gate")
time.sleep(1)

check_box = driver.find_elements(By.XPATH,"//input[@value= 'checkbox']")
for box in check_box:
    if check_box.index(box)+1 == 7 :        #  > 6 < 7:
        box.click()