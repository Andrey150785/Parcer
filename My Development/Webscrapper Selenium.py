from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
driver.get('https://www.example.com')

# Find the search box element (assuming there's a search box with the name 'q')
search_box = driver.find_element(By.NAME, 'q')

# Enter search term and hit Enter
search_box.send_keys('Python Data Science')
search_box.send_keys(Keys.RETURN)

# Wait for the results to load (implicit wait)
driver.implicitly_wait(10)

# Find the titles of the search results (assuming they are within <h2> tags)
titles = driver.find_elements(By.TAG_NAME, 'h2')

# Print the titles of the search results
for title in titles:
    print(title.text)

# Close the browser
driver.quit()