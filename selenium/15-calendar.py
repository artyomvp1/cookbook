import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
WATCH! : https://www.youtube.com/watch?v=0_-e2kbhXZM&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=77
"""
driver = webdriver.Chrome()
driver.get('https://www.yatra.com')
time.sleep(1)

# 1. Incorrect approach (hardcoding)
"""
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()  # Click on the calendar
time.sleep(2)
driver.find_element(By.ID, "28/11/2023").click()  # Click on a date
time.sleep(2)
"""

# 2. Correct date (collect all the elements in a list, use a loop). Tag tree
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()  # Click on the calendar
all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")  # All active dates
for i in all_dates:
    if i.get_attribute("data-date") == "15/11/2023":
        print(i.get_attribute("data-date"))
        i.click()
        break

time.sleep(5)
