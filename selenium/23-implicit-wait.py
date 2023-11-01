import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Waits in Selenium are dynamic, meaning as soon as web elements are presented Selenium performs the next stop.

Implicit wait - max amount of specified time we have to wait when searching a web element before throwing an exception.
Implicit wait is global and applicable to all web elements in the script.
No expected conditions are required.
"""
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Implicitly wait for 10 seconds for every step in the script!
driver.get('https://login.salesforce.com/')

driver.find_element(By.XPATH, "//input[@id='username']").send_keys("artyomvp1")
time.sleep(3)
