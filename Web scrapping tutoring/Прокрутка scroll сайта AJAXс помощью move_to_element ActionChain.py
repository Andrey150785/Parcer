from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as driver:

    action = ActionChains(driver)
    check = []
    total = 0
    stop = False
    driver.get('http://parsinger.ru/infiniti_scroll_1/')

    while True:
        for span in [_ for _ in driver.find_element(
                By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]:
            if span not in check:
                total += int(span.text)
                check.append(span)
                action.move_to_element(span).perform()
            if span.get_attribute('class') == 'last-of-list':
                stop = True
        if stop is True:
            break

    print(total)