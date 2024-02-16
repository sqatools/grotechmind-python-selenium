import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = None
wait = None

def launch_browser(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    time.sleep(5)
    return driver, wait


def mouse_hover():
    global driver, wait
    driver, wait = launch_browser("https://www.globalsqa.com/demo-site/frames-and-windows/")
    print(driver, wait)
    free_book = driver.find_element(By.XPATH, "//a[text()='Free Ebooks' and @class='no_border']")
    action = ActionChains(driver)
    action.move_to_element(free_book)
    action.perform()

    ml = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Free Machine Learning Ebooks']//parent::a")))
    action.move_to_element(ml)
    action.click()
    action.perform()
    time.sleep(10)

    tester_hub = driver.find_element(By.XPATH, "//a[text()='Tester’s Hub' and @class='no_border']")
    action.move_to_element(tester_hub)
    action.perform()
    time.sleep(10)

    demo_site = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Demo Testing Site']//parent::a[contains(@class,'no_border')]")))
    action.move_to_element(demo_site)
    action.perform()
    time.sleep(5)

    alert_box = wait.until(ec.visibility_of_element_located((By.XPATH, "(//span[text()='AlertBox']//parent::a)[1]")))
    action.move_to_element(alert_box)
    action.click()
    action.perform()
    time.sleep(5)

def drag_and_drop_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    iframe_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe_element)
    src = wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@alt='The peaks of High Tatras']//parent::li")))
    tar = wait.until(ec.visibility_of_element_located((By.ID, "trash")))
    action = ActionChains(driver)
    action.drag_and_drop(src, tar)
    action.perform()
    time.sleep(5)

def close_browser():
    driver.close()

mouse_hover()
drag_and_drop_operation()
close_browser()

