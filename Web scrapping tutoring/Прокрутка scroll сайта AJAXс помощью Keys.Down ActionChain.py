from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(2)
    while True:
        try:
            if browser.find_element(By.CLASS_NAME, 'last-of-list'):
                print('THE END OF SCROLL LIST IS FOUND')
                names = [int(i.text) for i in browser.find_elements(By.TAG_NAME, 'span') if i.text]
                print(sum(names))
                break
        except:
            browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)