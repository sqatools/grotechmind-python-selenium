from selenium.webdriver.common.by import By


amazon_start_here = (By.XPATH, "//a[text()='Login']")
amazon_create_account=(By.XPATH,"//a[contains(text(),'Create')]")
amazon_enter_email=(By.XPATH,"//input[contains(@class, '_2IX_2-')]")
amazon_click_continue=(By.XPATH,"//span[contains(text(),'CONTINUE')]")