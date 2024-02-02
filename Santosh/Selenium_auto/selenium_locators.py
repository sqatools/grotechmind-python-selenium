from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.get("https://www.goibibo.com/flights/?utm_source=bing&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only%20Goibibo&utm_term=!SEM!DF!B!Brand!RSA!150035352!1211662109442708!!e!goibibo!c!&msclkid=1321ac3960101e778eccc9820aad1882")
#f="Nanded"
# F_name="Santosh"
# driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys(F_name)
# driver.find_element(By.ID,"roundtrip").click()
# driver.find_element(By.NAME,"fromcity").send_keys(f)
# #driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[8]/td[1]/input").click()
# driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]").click()
# header = driver.find_element(By.TAG_NAME, "p").text
# print(header)

# var=driver.find_element(By.XPATH,"//h1[text()=' Dummy Ticket Booking Website']").text
# print(var)
var=driver.find_element(By.XPATH,"(//p[text()='Enter city or airport'])[1]").text
print(var)



#driver.find_element(By.XPATH,"//input[@value='radio_123' and @type='radio']").click()
#driver.find_element(By.XPATH,"//*[@value='radio2' and @name='radioButton']").click()

#driver.find_element(By.XPATH,"(//input[@name='firstname' and @id='firstname'])[2]").send_keys(f)

time.sleep(5)

driver.close()


#########################################################################################

