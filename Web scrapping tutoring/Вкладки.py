import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    count = 0
    browser.get('http://parsinger.ru/blank/3/index.html')
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'buttons')]
    time.sleep(5)
    tabs = browser.window_handles

    for tab in range(len(tabs)):
        browser.switch_to.window(browser.window_handles[tab])
        title = browser.execute_script("return document.title;")
        if title.isdigit():
            count += int(title)
    print(count)