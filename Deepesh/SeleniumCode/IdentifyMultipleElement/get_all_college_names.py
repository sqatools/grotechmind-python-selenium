from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://collegedunia.com/engineering/indore-colleges")

# element_list = driver.find_elements(By.XPATH, "//a[contains(@class, 'college_name')]/h3")
#
# for elem in element_list:
#     print(elem.text)

ranks = driver.find_elements(By.XPATH, "(//table[contains(@class, 'listing-table')])/tbody[1]/tr/td[1]")
college_names= driver.find_elements(By.XPATH, "(//table[contains(@class, 'listing-table')])/tbody[1]/tr/td[2]//h3")
collge_fees = driver.find_elements(By.XPATH, "(//table[contains(@class, 'listing-table')])/tbody[1]/tr/td[3]//a[@data-ga-event-category='courses-fees']/span[1]")
for i in range(len(ranks)):
    print(ranks[i].text, college_names[i].text)
    print("free amount :", collge_fees[i].text[1:])
    rank = ranks[i].text
    college_name = college_names[i].text
    college_fee = collge_fees[i].text[1:]


    with open("college_data.txt", "a+") as file:
        data = f"{rank}, {college_name} {college_fee}\n"
        file.write(data)



driver.close()