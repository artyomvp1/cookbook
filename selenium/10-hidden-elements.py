import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Some elements may be hidden until some actions are performed (button to show the hidden content).
To check if the element if hidden there is a method "is_displayed" (example 1) 
"""

# Example 1 (The element exists but hidden) #
driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
time.sleep(1)

# The web element is hidden
displayed1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(displayed1)

# Clicking the button to unhid the button
driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()

# The web element is not hidden
displayed2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(displayed2)

driver.close()


# Example 2 #
"""
The web element "age" appears only once the number of child becomes more than 1.
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com/hotels')
time.sleep(1)

driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()  # click on dropdown

# Element "age" will be available and displayed after setting "child > 1" by hitting "+"
driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()  # click on "child" +
displayed3 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
print(displayed3)

time.sleep(2)

# Element "age" will not be available after hitting "child < 1" by hitting "-". Hence error.
driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()  # click on "child" -
displayed4 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
print(displayed4)  # Will throw an error because the element does not exist. Need to use exception.

driver.close()
