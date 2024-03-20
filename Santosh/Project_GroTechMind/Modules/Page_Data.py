from selenium.webdriver.common.by import By



login_button=(By.XPATH,"(//a[text()='Login'])[1]")
sign_up=(By.XPATH,'//a[contains(text(),"Sign Up")]')
enter_email_id=(By.XPATH,"//input[@name='register_user_email']")
user_name=(By.XPATH,"//input[@name='register_user_login']")
user_password=(By.XPATH,"//input[@name='register_user_password']")
repeat_user_password=(By.XPATH,"//input[@name='register_user_password_re']")
checkbox=(By.XPATH,"(//span[@class='masterstudy-authorization__checkbox-wrapper'])[1]")
click_sign_up=(By.XPATH,"(//span[text()='Sign Up'])[2]")

#2) Validate the login functionality with valid credentials.

click_to_login=(By.XPATH,"//a[@id='masterstudy-authorization-sign-in']")
valid_user_name=(By.XPATH,"//input[@name='user_login']")
valid_password=(By.XPATH,"//input[@name='user_password']")
final_click_sing_in=(By.XPATH,"//span[text()='Sign In' and @class='masterstudy-button__title']")





