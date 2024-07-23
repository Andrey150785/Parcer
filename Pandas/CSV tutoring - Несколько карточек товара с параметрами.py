import requests
from bs4 import BeautifulSoup
import csv

with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])

url = 'http://parsinger.ru/html/index3_page_2.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
print((description))
price = [x.text for x in soup.find_all('p', class_='price')]

with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for item, price, descr in zip(name, price, description):
        flatten = [item, price, *[x.split(':')[1].strip() for x in descr if x]]
        writer.writerow(flatten)

