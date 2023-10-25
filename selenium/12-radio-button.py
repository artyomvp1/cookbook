import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Radio button is the same as checkboxed but round and you can select only one per time.
Has a method to check wether it is selected.
"""

driver = webdriver.Chrome()
driver.get('https://www.w3.org/WAI/UA/TS/html401/cp0101/0101-RADIO.html')
time.sleep(1)

driver.find_element(By.ID, "button2").click()
time.sleep(1)
driver.find_element(By.ID, "button1").click()
time.sleep(3)

state = driver.find_element(By.ID, "button1").is_selected()
print(state)
