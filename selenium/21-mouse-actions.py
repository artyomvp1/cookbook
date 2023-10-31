import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # Action chains class to control mouse (move, click, double click etc.)

"""
Handling right and double click using ActionChain class
"""
driver = webdriver.Chrome()
driver.get('https://demo.guru99.com/test/simple_context_menu.html')
driver.maximize_window()
time.sleep(8)

# Creating instance of ActionChains class
action_chain = ActionChains(driver)

# Right click using context_click()
action_chain.context_click(driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")).perform()  # chain always ends with perfom()
time.sleep(2)

# Click the element in the menu after right click
driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
time.sleep(2)

# Double click
# Same approach for double click
