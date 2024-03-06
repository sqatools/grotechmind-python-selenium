from selenium.webdriver.common.by import By

flight_from_field = (By.XPATH, "//span[text()='From']//following-sibling::p")
flight_from_field_input = (By.XPATH, "//span[text()='From']//following-sibling::input")
flight_to_field = (By.XPATH, "//span[text()='To']//following-sibling::p")
flight_to_field_input = (By.XPATH, "//span[text()='To']//following-sibling::input")
mobile_login_popup = (By.XPATH, "//span[@class='logSprite icClose']")
date_picker_done_button = (By.XPATH, "//span[text()='Done']")
adults_plus_icon = (By.XPATH, "//p[text()= 'Adults']//parent::div//span[3]")
children_plus_icon = (By.XPATH, "//p[text()= 'Children']//parent::div//span[3]")
infants_plus_icon = (By.XPATH, "//p[text()= 'Infants']//parent::div//span[3]")
travel_class_done_button = (By.XPATH, "//a[text()='Done']")





