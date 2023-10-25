import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Checkboxes have web element type='Checkbox'.
There is a method to check whether a checkbox is selected.
"""

driver = webdriver.Chrome()
driver.get('https://www.yatra.com')
time.sleep(1)

driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").click()
time.sleep(5)
state = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_selected() # Is checkbox selected?
print(state)
