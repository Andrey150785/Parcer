import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with (webdriver.Chrome() as browser):
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    # item = browser.find_element(By.TAG_NAME, 'span')
    # for item in items:
    #     print(True)
    blocks = browser.find_elements(By.XPATH, "//div[contains(@style, 'background-color')]")
    for block in blocks:
        hex_color = block.find_element(By.TAG_NAME, 'span').text
        # print(hex_color)
        listed = block.find_elements(By.TAG_NAME, 'option')
        for i in listed:
            if i.text == hex_color:
                i.click()
        btns = block.find_elements(By.TAG_NAME, 'button')
        for i in btns:
         if i.get_attribute('data-hex') == hex_color:
                i.click()
        check1, txt1 = block.find_elements(By.TAG_NAME, 'input')
        check1.click()
        txt1.send_keys(hex_color)
        for i in btns:
            if i.text == 'Проверить':
                i.click()

    browser.find_element(By.XPATH, "//body/button").click()
    # time.sleep(10)
    alert = browser.switch_to.alert
    print(alert.text)





#         blue.send_keys(gray.text)
#         gray.clear()
#         item.find_element(By.TAG_NAME, 'button').click()
#     # Переключаемся на алерт
#     browser.find_element(By.ID, "checkAll").click()
#     time.sleep(5)
#     res = browser.find_element(By.ID, 'congrats').text
#     # Получаем текст с алерта
#     # alert_text = alert.text
#
# print(res)