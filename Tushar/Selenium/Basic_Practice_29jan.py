from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://www.goibibo.com/")

#driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p[text()='Enter city or airport']").send_keys('pune')
#driver.find_element(By.XPATH,"//input[@type='text']").send_keys('pune')

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#Self
#driver.find_element(By.XPATH,"//a[contains(text(),'Mahindra L')]").click()
#comp_name=driver.find_element(By.XPATH,"//a[contains(text(),'Mahindra L')]").text
#print(comp_name) #Mahindra Lifespaces calls off 5-acre joint development in Mumbai’s Dahisar

#parent

# parent_text=driver.find_element(By.XPATH,"//a[contains(text(),'Mahindra L')]//parent::td").text
# print(parent_text) #Mahindra Lifespace D

#child
#child_ele=driver.find_element(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//child::td").text
#print(child_ele) #Mahindra Lifespace D

#child_ele=driver.find_elements(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//child::td")
#print(len(child_ele)) #10

#ancenstor_text=driver.find_element(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr").text
#print(ancenstor_text) #Mahindra Lifespace D A 567.25 617.10 + 8.79

#descendant

#descendant_text=driver.find_elements(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//descendant::*")
#print(len(descendant_text)) #7

#followings=driver.find_elements(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//following::*")
#print(len(followings)) #2318


#following siblings

#following_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//following-sibling::*")
#print(len(following_sib)) #275

#preceding

#preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//preceding::tr")
#print(len(preceding)) #15

#preceding sibling

#pre_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Mahindra L')]//ancestor::tr//preceding-sibling::tr")
#print(len(pre_sib)) #16




time.sleep(5)
driver.close()
