import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
FIND_ELEMENTS method finds multiple elements and put them in a list so you can itterate.
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com')
driver.maximize_window()
time.sleep(2)

sequence = driver.find_elements(By.TAG_NAME, 'a')  # creates a list of tags with 'a'
print(len(sequence))  # prints it

for i in sequence:
    print(i.text)  # print the content of the tag

driver.close()
