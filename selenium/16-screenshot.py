import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
Screenshot can be make over a whole page or over a web element. 
Provide a location to store the screenshot.
"""
driver = webdriver.Chrome()
driver.get('https://secure.yatra.com/social/common/yatra/register')
time.sleep(1)

# Screenshot of a web element
button = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
button.screenshot("/Users/artyompak/Python/test/SeleniumTest/button.png")
time.sleep(1)

# Screenshot of a whole page
button.click()
driver.get_screenshot_as_file("/Users/artyompak/Python/test/SeleniumTest/page1.png")
time.sleep(2)

driver.save_screenshot("/Users/artyompak/Python/test/SeleniumTest/page2.png")  # same as get_screenshot
