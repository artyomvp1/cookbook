import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.yatra.com')
time.sleep(2)

text1 = driver.find_element(By.XPATH, "//a[normalize-space()='View All']").text

print(text1)

driver.close()
