# XPath and CSS Selectors are the ways to locate dynamic web elements (not unique)(you cannot find to find UNIQUE ID). 
# Just execute the following

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
driver.maximize_window()

time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('Artyom')  # Typing 'Artyom'

time.sleep(5)
driver.close()
