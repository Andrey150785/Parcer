import csv
import requests
from bs4 import BeautifulSoup

# 1 ------------------------------------------------------

url = 'https://parsinger.ru/html/index1_page_1.html'
site = 'https://parsinger.ru/html/'
name = [] #a class="name_item"
brand = [] #<li>Бренд: Jet</li>
type = [] #<li>Тип: умные часы</li>
corpus_material = [] #<li>Материал корпуса: пластик</li>
screen = [] #<li>Технология экрана: Монохромный</li>
price = [] #<div class="price_box"><p class="price">2310 руб</p></div>
description = []

for i in range(1, 6):
    for j in range(1, 5):
        url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name.extend([x.text for x in soup.find_all('a', class_='name_item')])
        price.extend([x.text for x in soup.find_all('p', class_='price')])
        description.extend([x.text.split('\n') for x in soup.find_all('div', class_='description')])

# print(description)
with open('result1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for n, p, d in zip(name, price, description):
        flatten = n, *[x.split(':')[1].strip() for x in d if x], p
        writer.writerow(flatten)

# for item in LINKS:
#     response = requests.get(url=item)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     name.append(soup.find('div', class_='description').find('p', id='p_header').text)
#     article.append(soup.find('div', class_='description').find('p', class_='article').text.split(':')[1].strip())
#     description = [i.text.split(':')[1].strip() for i in soup.find_all('li')]
#     brand.append(description[0])
#     model.append(description[1])
#     type_in.append(description[2])
#     screen.append(description[3])
#     corpus_material.append(description[4])
#     brasselet_material.append(description[5])
#     size.append(description[6])
#     company_site.append(description[7])
#     amount.append(soup.find('span', id='in_stock').text.split(':')[1].strip())
#     price.append(soup.find('span', id='price').text)
#     old_price.append(soup.find('span', id='old_price').text)
#     cards = list(
#         zip(name, article, brand, model, type_in, screen, corpus_material, brasselet_material, size, company_site,
#             amount, price, old_price, LINKS))
#
# # Открываем файл для дополнительной записи данных
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     for item in cards:
#         writer.writerow(item)
#
# # print(cards)
# print('Файл res.csv создан')