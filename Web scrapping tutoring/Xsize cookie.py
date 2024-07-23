from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

site = 'https://parsinger.ru/methods/5/'
D = []
expire = 0
result = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    links = browser.find_elements(By.CLASS_NAME, 'urls')
    for link in links:
        real_link = site + link.text
        # print(real_link)

with webdriver.Chrome() as webdriver:
    for i in range(1, 43):
        webdriver.get(f'https://parsinger.ru/methods/5/{i}.html')
        cookie = webdriver.get_cookie('foo2')
        if int(cookie['expiry']) > expire:
            expire = int(cookie['expiry'])
            result = webdriver.find_element(By.ID, 'result')
            pprint(result.text)
            # id = "result" > INT < / p >

        # pprint(cookies['expiry'])
    # for i in cookies:
    #     pprint(int(i['expiry']))
        # summa += int(i['value'])
        # pprint(summa)
