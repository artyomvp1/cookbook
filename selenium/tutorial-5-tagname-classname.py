import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
driver.maximize_window()
time.sleep(2)

# driver.find_element(By.TAG_NAME, 'input').send_keys('Test@test.com')  # Not reliable, since tags are not always unique
driver.find_element(By.CLASS_NAME, 'yt-sme-mobile-input required_field email-login-box').send_keys('NewValue@test.com')  # as you see there are 3 classes. CHOOSE ONE
time.sleep(5)

driver.close()
