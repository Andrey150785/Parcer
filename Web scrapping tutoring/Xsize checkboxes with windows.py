from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

dict_1 = {}

with (webdriver.Chrome() as driver):
    action = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.8/3/index.html')
    elements = driver.find_element(By.CLASS_NAME, 'main').find_elements(By.CLASS_NAME, 'pin')
    for el in elements:
        pin = el.text
        driver.find_element(By.ID, 'check').click()
        alert_window = driver.switch_to.alert
        alert_window.send_keys(pin)
        # print(code)
        alert_window.accept()
        # result = driver.find_element(By.CSS_SELECTOR, "div .res")
        # result.find_element(By.ID, 'input').send_keys(code)
        # time.sleep(0.3)
        info = driver.find_element(By.ID, 'result').text
        if info != "Неверный пин-код":
            print(info)
            break