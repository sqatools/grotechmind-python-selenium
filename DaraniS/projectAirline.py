from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.booking.com/")

#1.register
# driver.find_element(By.XPATH,"//span[contains(text(), 'Register')]").click()
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("durgasunkara90@gmail.com")
# driver.find_element(By.XPATH,"//span[contains(text(), 'Continue')]").click()
# driver.find_element(By.XPATH,"//input[@name='new_password']").send_keys("Darani@123")
# driver.find_element(By.XPATH,"//input[@name='confirmed_password']").send_keys("Darani@123")
# driver.find_element(By.XPATH,"//span[contains(text(), 'Create account')]").click()


#2.sign in
# driver.find_element(By.XPATH,"//span[text()='Sign in']").click()
# driver.find_element(By.XPATH,"//input[@id='username']").send_keys("durgasunkara90@gmail.com")
# driver.find_element(By.XPATH,"//span[contains(text(), 'Continue')]").click()
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Darani@123")
# driver.find_element(By.XPATH,"(//span[contains(text(),'Sign in')])[1]").click()

#3.Test login with invalid credentials a
# driver.find_element(By.XPATH,"//span[text()='Sign in']").click()
# driver.find_element(By.XPATH,"//input[@id='username']").send_keys("durgasunkara90@gmail.com")
# driver.find_element(By.XPATH,"//span[contains(text(), 'Continue')]").click()
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("123")
# driver.find_element(By.XPATH,"(//span[contains(text(),'Sign in')])[1]").click()
time.sleep(3)
#4.Test the search functionality for one-way flights
driver.find_element(By.XPATH,"//a[@id='flights']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='One way']").click()
#driver.find_element(By.CSS_SELECTOR,"button[fdprocessedid='wf82oq']").click()
driver.find_element(By.XPATH,"//button[@data-ui-name='input_location_to_segment_0']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Airport or city']").send_keys("Montreal")


time.sleep(30)

driver.close()