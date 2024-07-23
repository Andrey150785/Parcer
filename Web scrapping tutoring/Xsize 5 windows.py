from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

total = 0
mask = 'scroll-container_'

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_3/')
    action = ActionChains(driver)
    for window in [f'scroll-container_{i}' for i in range(1, 6)]:
        print(window)
        check = []
        stop = False
        while True:
            for element_span in [span for span in driver.find_element(
                    By.ID, window).find_elements(By.TAG_NAME, 'span')]:
                if element_span not in check:
                    total += int(element_span.text)
                    check.append(element_span)
                    action.move_to_element(element_span).perform()
                if element_span.get_attribute('class') == 'last-of-list':
                    stop = True
            if stop is True:
                action.reset_actions()
                break

print(total)

