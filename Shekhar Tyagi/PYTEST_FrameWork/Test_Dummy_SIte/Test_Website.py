from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_data import *
import time

def test_Website(browser):
# it is for select the radio button.
	browser.get(website_url4)
	time.sleep(1)
	browser.find_element(By.CSS_SELECTOR, "input[value='radio1']").click()
	time.sleep(1)
	browser.find_element(By.CSS_SELECTOR, "input[value=radio2]").click()
	time.sleep(1)
	browser.find_element(By.CSS_SELECTOR, "input.radioButton[value=radio3]").click()
	time.sleep(2)
	browser.find_element(By.XPATH, "//*[@value='radio2' and @name='radioButton']").click()

def test_the_TextBox(browser):
# it is use for enter the text or value.
	Name= browser.find_element(By.XPATH, "//*[@id='name']")
	time.sleep(1)
	Name.send_keys(Name1)
	time.sleep(2)
# it is use for clear the text from the text box.
	Name.clear()
	time.sleep(1)
	Name.send_keys(Name2)

def test_alart(browser):
	Alert = browser.find_element(By.XPATH, "//legend[normalize-space()='Switch To Alert Example']")
	Alert1 = Alert.text
	print("\n",Alert1)

def test_checlbox(browser):
	# it is use for select the multi check-Box with for loop condition.

	check_boxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
	for check_box in check_boxes:
		if check_boxes.index(check_box) + 1 != 2:
			check_box.click()
	print("\n",check_boxes)
	print("\n",len(check_boxes))
	time.sleep(1)

def test_dropdown(browser):
# it is use for select the value from dropdown list. 3 mathods is used for select the dropdown value.

	static_dropdown = browser.find_element(By.ID, "dropdown-class-example")
	select = Select(static_dropdown)
	select.select_by_index(2)
	time.sleep(2)
	select.select_by_value("option1")
	time.sleep(2)
	select.select_by_visible_text("Option3")
	time.sleep(2)

def test_option(browser):
# it is use for direct selection from dropdown list.

	drop = browser.find_element(By.XPATH, "//option[@value='option2']").click()
def test_lint(browser):
# get attribute mathod is use for get the anu url from website.

	links = browser.find_element(By.CLASS_NAME, "blinkingText")
	print("Lint_Test: ","\n",links.get_attribute("href"))




