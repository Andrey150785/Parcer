from selenium import webdriver
import time
from selenium.webdriver.common.by import By

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    # Открываем указанный URL в браузере.
    browser.get('https://parsinger.ru/window_size/2/index.html')

    for i in window_size_x:
        for j in window_size_y:
            # Устанавливаем размер окна браузера на 1200 пикселей в ширину и 720 пикселей в высоту.
            browser.set_window_size(i+13, j+136)
            try:
                res = browser.find_element(By.ID, 'result').text
                if res:
                    print(browser.get_window_size())
                    break
            except:
                continue
            time.sleep(4)