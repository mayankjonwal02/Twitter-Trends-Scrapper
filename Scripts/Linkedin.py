from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create instance of Chrome webdriver
driver = webdriver.Chrome()

# Open Twitter login page
driver.get("https://www.linkedin.com/home")

# Wait for the username/phone/email field to be visible
time.sleep(5)

# Find and fill the username/phone/email field
driver.find_element(By.XPATH, '//*[@id="session_key"]').send_keys('jonwal.1@iitj.ac.in')
driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys('Mayjon@1372')
driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()

# Wait for the password field to be visible
time.sleep(5)



# Close the browser
driver.quit()
