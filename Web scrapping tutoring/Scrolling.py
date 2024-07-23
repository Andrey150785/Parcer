from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

site = 'https://parsinger.ru/scroll/4/index.html'
summa = 0

with webdriver.Chrome() as browser:
    browser.get(site)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    for button in buttons:
        # print(button.text)
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        summa += int(browser.find_element(By.ID, "result").text)

print(summa)