import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
Sometimes after clicking a browser opens another tab. Selenium can handle it. 
Each tab(window) has a unique ID, using which Selenium can control the process.
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com/')
driver.maximize_window()

parent_handle = driver.current_window_handle  # Parent window ID
print(parent_handle)
time.sleep(1)

driver.find_element(By.XPATH, "//a[@title='Niyo Global']//img[@class='conta iner large-banner']").click()
# New tab is opening but Selenium is still on the parent page.
time.sleep(3)

# Get all available window handles (IDs)
all_window_handles = driver.window_handles
print(all_window_handles)

# Switch to the child handle (tab)
for i in all_window_handles:  # Going through all available handles
    if i != parent_handle:
        driver.switch_to.window(i)  # Switching to the handle which is not parent

        # Now the focus on the child window
        driver.find_element(By.XPATH, "(//button[@id='contact_formcor'])[1]").click()
        time.sleep(5)
        driver.close()  # closing the child tab
        time.sleep(5)
        break

# We have to manually switch to parent window
driver.switch_to.window(parent_handle)
time.sleep(1)

driver.find_element(By.XPATH, "//a[@title='Niyo Global']//img[@class='conta iner large-banner']").click()
