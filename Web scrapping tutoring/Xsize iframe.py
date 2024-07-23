from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with (webdriver.Chrome() as driver):
    action = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')
    elements = driver.find_element(By.ID, 'main_container').find_elements(By.TAG_NAME, 'iframe')
    for i in elements:
        driver.switch_to.frame(i)
        time.sleep(0.2)
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(0.2)
        code = driver.find_element(By.ID, 'numberDisplay').text
        # print(code)
        driver.switch_to.default_content()
        # result = driver.find_element(By.CSS_SELECTOR, "div .res")
        driver.find_element(By.ID, 'guessInput').clear()
        driver.find_element(By.ID, 'guessInput').send_keys(code)
        # time.sleep(0.3)
        info = driver.find_element(By.ID, 'checkBtn').click()
        time.sleep(0.2)
        try:
            alert_window = driver.switch_to.alert
            print(alert_window.text)
            alert_window.accept()
        except:
            # continue
            pass
    #
    # if info != "Неверный пин-код":
    #     print(info)
    #     break