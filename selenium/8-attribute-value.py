import time
from selenium import webdriver
from selenium.webdriver.common.by import By

""" 
Webelements may contain attributes, data-role, type, value, id, class, etc.
<input data-role="none" type="submit" value="Search Flights" id="BE_flight_flsearch_btn" class="js_ripple search-btn " xpath="1"> - this is a web element.
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com')
time.sleep(2)

attr = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")  # get_attribute() - method to get

print(attr)
driver.close()
