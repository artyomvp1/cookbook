from selenium import webdriver


driver = webdriver.Chrome()  # Path is not required in the latest selenium
driver.get('https://www.meduza.io')  # https is required

# Get title
print(driver.title)

# Maximize window
driver.maximize_window()  # maximize window

# Close browser
driver.close()  # close current browser, quit() all assosiated browsers
