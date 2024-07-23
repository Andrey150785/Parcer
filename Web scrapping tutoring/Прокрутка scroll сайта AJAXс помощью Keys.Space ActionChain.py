from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/infiniti_scroll_1/")
    actions = ActionChains(driver)

    while True:
        actions.send_keys_to_element(driver.find_element(By.ID, "scroll-container"), Keys.SPACE).perform()
        try:
            driver.find_element(By.CSS_SELECTOR, "span.last-of-list")
            break
        except NoSuchElementException:
            continue

    print(sum(int(i.text) for i in driver.find_elements(By.XPATH, "//div/div[@id='scroll-container']/span")))