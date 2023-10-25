from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
driver.maximize_window()
driver.find_element(By.ID, "login-input").send_keys('Test')  # special library for By

driver.close()
