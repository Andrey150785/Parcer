from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

check = []

with webdriver.Chrome() as driver:
    action = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')

    while len(check) <100:
        elements = driver.find_element(By.ID, 'main_container').find_elements(By.CLASS_NAME, 'child_container')
        # print(len(elements))
        for element in elements:
            if element not in check:
                # for x in [y for y in element.find_elements(By.TAG_NAME, 'input') if int(y.get_attribute('value')) % 2 == 0]:
                #     x.click()
                check.append(element)
                action.move_to_element(element).perform()
            # time.sleep(1)
    for x in [y for y in driver.find_element(By.ID, 'main_container').find_elements(By.TAG_NAME, 'input') if int(y.get_attribute('value')) % 2 == 0]:
                x.click()
    driver.find_element(By.CLASS_NAME, 'alert_button').click()
    time.sleep(2)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()