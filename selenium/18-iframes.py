import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
iFrame - window in a window. You have to switch iframe to interact with elements. 
Find iframes in the web elements, inspect: <iframe src = ...>. 
Always understand how iframes are structured in the page you are testing.
iFrames can be nested so in order to reach the target frame we have to switch layer by layer.
You can switch iframes using XPATH, name etc. or index.
"""
driver = webdriver.Chrome()
driver.get('https://seleniumbase.io/w3schools/iframes')
driver.maximize_window()
time.sleep(3)

# Click on the link - will fail because we are on the parrent (white left iframe)
"""
driver.find_element(By.XPATH, "//a[normalize-space()='seleniumbase.io/w3schools/iframes']").click()
"""

# Switching to the iframe the element belongs to + clicking the element
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))  # switching to the 1st child (white right)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Iframe Example']"))  # switching to the 2nd child (blue)
time.sleep(1)

driver.find_element(By.XPATH, "//a[normalize-space()='seleniumbase.io/w3schools/iframes']").click()
time.sleep(5)
