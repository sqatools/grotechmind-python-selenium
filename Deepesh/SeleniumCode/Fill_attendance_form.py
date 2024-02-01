from selenium import webdriver
from selenium.webdriver.common.by import By
import time

name = "Deepesh Yadav"
batch_name = "Python Selenium Batch 02"
check_in1 = "08"
check_in2 = "00"

check_out1 = "08"
check_out2 = "00"

recording_title = "Python Programming"
def fill_attendance_form(date, present=True):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdJDvvFj36h2pyvpPoIWdSWx4qx4AI4_KKZBoLUs2cfPfPMDA/viewform")
    # set name
    time.sleep(10)
    driver.find_element(By.XPATH, "//span[text()='Name']//ancestor::div[@role='listitem']//input").send_keys(name)
    # set date
    driver.find_element(By.XPATH, "//span[text()='Date']//ancestor::div[@role='listitem']//input").send_keys(date)
    # Attendance Confirmation
    if present:
        driver.find_element(By.XPATH, "(//span[text()='Attendance Confirmation']//ancestor::div[@role='listitem']//label)[1]").click()
    else:
        driver.find_element(By.XPATH,
                        "(//span[text()='Attendance Confirmation']//ancestor::div[@role='listitem']//label)[2]").click()
    # Course Handling
    driver.find_element(By.XPATH, "(//span[text()='Course Handling']//ancestor::div[@role='listitem']//label)[4]").click()
    driver.find_element(By.XPATH, "(//span[text()='Course Handling']//ancestor::div[@role='listitem']//input)[2]").send_keys(batch_name)
    # Check-in time
    driver.find_element(By.XPATH, "(//span[text()='Check -In']//ancestor::div[@role='listitem']//input)[1]").send_keys(check_in1)
    driver.find_element(By.XPATH, "(//span[text()='Check -In']//ancestor::div[@role='listitem']//input)[2]").send_keys(check_in2)

    # Check-out time
    driver.find_element(By.XPATH, "(//span[text()='Check-out']//ancestor::div[@role='listitem']//input)[1]").send_keys(check_out1)
    driver.find_element(By.XPATH, "(//span[text()='Check-out']//ancestor::div[@role='listitem']//input)[2]").send_keys(check_out2)

    # Duration of the class
    driver.find_element(By.XPATH, "(//span[text()='Duration of the class']//ancestor::div[@role='listitem']//label)[4]").click()

    # Uploaded the recording to the application
    driver.find_element(By.XPATH, "(//span[text()='Uploaded the recording to the application']//ancestor::div[@role='listitem']//label)[1]").click()

    #Tittle of the Recording
    driver.find_element(By.XPATH, "//span[text()='Tittle of the Recording']//ancestor::div[@role='listitem']//input").send_keys(recording_title)
    time.sleep(5)
    # submit button
    driver.find_element(By.XPATH,"//span[text()='Submit']").click()

    time.sleep(2)
    driver.close()

date_list = ["01/23/2024", "01/24/2024", "01/25/2024", "01/26/2024",
             "01/29/2024", "01/30/2024", "01/31/2024"]

for date in date_list:
    print(date)
    fill_attendance_form(date)