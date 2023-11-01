import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # class for explicit wait
from selenium.webdriver.support import expected_conditions as EC  # class for expected condition to end explicit wait

"""
Speed of the script may not be in sync with the application.
To implement explicit wait we need to import the class WebDriverWait.
Explicit wait tells the web driver to halt the execution until a certain condition is met or max time has passed.
Explicit wait is specific to web element, meaning applicable for the elements defined by users.
Requires expected conditions.
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com')

# Create instance for explicit wait (seconds how long to wait)
wait = WebDriverWait(driver, 10)

# Check condition (is clickable, visible, exist, text presented, etc.) and then perform action
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']"))).click()
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").send_keys('Tashkent')

time.sleep(5)
