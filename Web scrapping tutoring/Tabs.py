import time
from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
i = 1

summa = 0

with webdriver.Chrome() as browser:
    for site in sites:
        browser.execute_script(f'window.open("{site}", "_blank_{i}");')
        i += 1
        if i>6:
            break
    tabs = browser.window_handles
    for tab in range(len(tabs)-1):
        if not browser.execute_script("return document.title;"):
            browser.close()
        browser.switch_to.window(browser.window_handles[tab])
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        el = int(browser.find_element(By.ID, 'result').text)**0.5
        summa += el

print(round(summa, 9))
