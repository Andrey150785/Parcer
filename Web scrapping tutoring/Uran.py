from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for button in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)


