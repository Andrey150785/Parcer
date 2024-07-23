import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

password = ""
counter = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    for elem in browser.find_elements(By.CLASS_NAME, "box_button"):
        counter += 1
        elem.click()
        # time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "#ad_window #close_ad").click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, "ad_window")))
        # time.sleep(3)
        code = elem.text
        password += code
        if counter < 9:
            password += "-"
        else:
            break
    # elements = browser.find_elements(By.CLASS_NAME, "box_button")
    # # print(elements)
    # for element in elements:
    #     element.click()
    #     browser.find_element(By.CSS_SELECTOR, "#ad_window #close_ad").click()
    #     WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, "ad_window")))
    #     code = element.text
    #     password += code
    print(password)
