import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Alert are the popup windows with warning.
You can accept, dismiss, send or get text to the alert.
"""
driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm')
driver.maximize_window()
time.sleep(2)

# Triggering popup window
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
time.sleep(2)

# Once alert is appeared you need to switch to the alert
driver.switch_to.alert.accept()  # accept(), dismiss(), send_keys(), text()
