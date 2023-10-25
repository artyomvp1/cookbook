import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select   # Class to select from a dropdown

"""
To handle selection in dropdowns we use class Select and its methods.
The values in the dropdown can be selected by index, visible text or value.
"""
driver = webdriver.Chrome()
driver.get('https://www.salesforce.com/au/form/signup/freetrial-sales/')
time.sleep(1)

# Working with the dropdown element
dropdown = driver.find_element(By.NAME, "UserTitle")
d = Select(dropdown)

d.select_by_index(1)  # Position of the value in the dropdown. The value may be disabled (check web element attributes)
time.sleep(3)

d.select_by_visible_text("Customer Service Manager")  # Check the attributes
time.sleep(3)

d.select_by_value("Sales_Manager_ANZ")  # Check the value in the element attributes (value=)
time.sleep(3)
