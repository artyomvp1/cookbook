import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Some elements may be disabled and are enabled only after some actions like inputting login or password.
To find whether a web element is disabled or enabled there is a method "is_enabled()"
"""

driver = webdriver.Chrome()
driver.get('https://training.openspan.com/login')
time.sleep(1)

# Button is disabled
state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()  # function returning boolean
print(state1)

# Button is enabled after posting login pass
driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys('artyomvp1')
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys('Liverpool')
state2 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()  # function returning boolean
print(state2)

driver.close()
