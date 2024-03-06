from selenium.webdriver.common.by import By

read_only_reg=(By.XPATH,"(//a[@href='https://grotechminds.com/registration/'])[1]")
reg_email=(By.XPATH,"//input[@id='email']")
reg_password=(By.XPATH,"//input[@id='password']")
reg_female=(By.XPATH,"//input[@id='Female']")
reg_skills=(By.XPATH,"(//div[@id='skillsDropdown'])[1]")
reg_skills_drop=(By.XPATH,"//li[text()='Technical Skills']")