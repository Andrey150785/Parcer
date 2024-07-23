import time
from faker import Faker as f #Библиотека с фейковыми данными пользователей
from selenium import webdriver
from selenium.webdriver.common.by import By
import random as rd

# Создаем фейковые данные пользователя
f = f("RU")
form_list = [f.first_name_male(),f.last_name_male(),f.middle_name_male(),rd.randint(10,99),f.city_name(),f.email()]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'form')
    for form, user_data in zip(input_form, form_list):
        form.send_keys(user_data)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    secret_code = browser.find_element(By.ID, 'result').text
    time.sleep(5)

print(f'Пользователь с данными: {form_list} авторизован')
print(f'Результат: {secret_code}')