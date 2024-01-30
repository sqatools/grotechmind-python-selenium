from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

options = Options()
options.add_experimental_option( "detach", True)
driver= webdriver.Chrome(options= options)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.ixigo.com/")
time.sleep(4)
driver.find_element(By.XPATH,"//span[contains(text(),'Hotels')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@value='Goa']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='ml-auto self-end']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(@class,'flex-1 flex-shrink-0 text-neutral-800 cursor-pointer rounded-l-10 bg-surface-tertiary pt-10 border-primary-500 flex cursor-pointer px-15')]//input[contains(@class,'w-full focus:outline-none bg-transparent h6 font-medium truncate InputDesktop_input__8ZbNC')]").send_keys("Bengaluru")
time.sleep(1)
driver.find_element(By.XPATH," //p[normalize-space()='Bengaluru']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//abbr[contains(@aria-label,'March 20, 2024')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//abbr[contains(@aria-label,'April 1, 2024')][normalize-space()='1'])[2]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[@data-testid='room-increment']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[contains(@data-testid,'adult-increment')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[contains(@data-testid,'adult-decrement')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[@data-testid='counter-increment-children']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//option[@value='2']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Done']").click()
driver.find_element(By.XPATH,"//div[contains(@class,'flex items-center gap-5 font-medium')]").click()
time.sleep(1)




