import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # class to manipulate keyboard

"""
WATCH!: https://www.youtube.com/watch?v=ofag5jbT-Pc&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=75
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com')
time.sleep(1)

# Scenario 1: Click the field, fill out, hit enter
depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
depart_from.click()
time.sleep(2)

depart_from.send_keys("New Delhi")
time.sleep(2)

depart_from.send_keys(Keys.ENTER)
time.sleep(1)

# Scenario 2: Choosing from auto-suggestion
going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
going_to.send_keys("New")  # Printing 'New'

search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")  # find_elementS - return a list. getting the list of all of the auto-suggestions
print(len(search_results))

for i in search_results:  # going through the list and click if matching
    if "New York (JFK)" in i.text:
        i.click()
        time.sleep(4)
        break
