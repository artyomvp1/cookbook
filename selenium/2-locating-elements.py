from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Library to locate "by"

"""
Find web element locators using 'inspect' functionality.
You can inspect by mouse.
"""
driver = webdriver.Chrome()
driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
driver.maximize_window()

# Locating an element
driver.find_element(By.ID, "login-input").send_keys('Test')  # Sending text "test" to the field

driver.close()
