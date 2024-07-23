from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/4/index.html")
    balls = driver.find_elements(By.CLASS_NAME, "ball_color")
    targets = driver.find_elements(By.CLASS_NAME, "basket_color")
    message = driver.find_element(By.CLASS_NAME, "message")
    actions = ActionChains(driver)

    for ball in balls:
        for target in targets:
            if target.get_attribute("class").split()[1] == (ball.get_attribute("class").split()[1]).split("_")[0]:
                actions.drag_and_drop(ball, target).perform()

    print(message.text)

    # for ball in balls:
    #     if
    #
    # print(driver.find_element(By.ID, "message").text)
    # Пауза для визуальной проверки результата
    # time.sleep(5)