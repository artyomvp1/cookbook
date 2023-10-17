import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.yatra.com/')
driver.maximize_window()
time.sleep(2)

driver.find_element(By.LINK_TEXT, 'Yatra for Business').click()
time.sleep(5)

driver.close()

# Also can identify by partial linked text method
