import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # Action chains class to control mouse (move, click, double click etc.)

"""
Some web elements are visible only when you point using a mouse.
Otherwise they are not available to interact.
To create mouse actions we use ActionChains class from Selenium library.
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com/')
driver.maximize_window()
time.sleep(1)

# Action chain must always end with perform() method (click().perform())
action_chain = ActionChains(driver)  # Instance to control

# Hovering a mouse over the element with a hidden menu
action_chain.move_to_element(driver.find_element(By.XPATH, "//span[@class='more-arr']")).perform()  # moving the mouse to the element "More" and perform (right click, double click etc)
time.sleep(2)

# Now mouse hover menu is displayed and available for interaction
driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
time.sleep(2)
