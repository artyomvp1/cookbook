import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # Action chains class to control mouse (move, click, double click etc.)

"""
Drag and drop using ActionChains.
Put 'from' element to drag and 'to' element to drop.
You can also drag and drop by coordinates (by offset). You need to know the coordinates.
"""
driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')
driver.maximize_window()
time.sleep(1)

# Switch to the frame (since drag and drop in a separate frame)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

# Create action chain instance
action_chain = ActionChains(driver)

# Perform drag and drop
from_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
to_element = driver.find_element(By.XPATH, "//div[@id='droppable']")
action_chain.drag_and_drop(from_element, to_element).perform()

time.sleep(5)
