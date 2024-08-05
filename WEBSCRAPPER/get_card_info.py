import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools
import lxml
import csv
import datetime
from time import perf_counter as pf
from prettytable import PrettyTable

HOST = "https://novosibirsk.n1.ru/"
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10&rooms=1&is_newbuilding=false&total_area_min=30&total_area_max=50&release_date_min=2000&floor_not_first=true&floors_count_min=10"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
url = 'https://novosibirsk.n1.ru//view/108168828/'

table = PrettyTable() #Создаем таблицу для красивого вывода в консоль
columns = ['Количество комнат', 'Улица', '№ дома', 'Площадь', 'Этаж', 'Этажей в доме', 'Цена', 'Дата публикации',
      'Количество просмотров', 'Декларация', 'Описание', 'Собственность', 'Год постройки', 'Материал стен', 'Агентство',
      'Продавец', 'Телефон']
table.field_names = columns

def get_info(url):
    flat_row = [] # Список из полученных параметров и характеристик квартиры из карточки
    # функция, собирающая информацию из карточки объявления о квартире
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    rooms = [int(x) for x in soup.find('span', class_='deal-title').text if x.isdigit()][0]
    street = (soup.find('span', class_='address').text).strip(', ')
    number = (soup.find('span', class_='house-number').text).strip(', ')
    price = int(''.join([x for x in (soup.find('span', class_='price').text).strip(' ') if x.isdigit()]))
    publish_date = (soup.select_one("div[class='trigger'] div").text).strip() # дату нужно еще постараться вытянуть
    refresh_date = [x.text.strip() for x in soup.find('div', class_='meta').find_all('span', class_='label')][0] # дату нужно еще постараться вытянуть
    visits = [x.text.strip() for x in soup.find('div', class_='meta').find_all('span', class_='label')][1]
    try:
        declaration = soup.find('p', class_='card-living-content-declaration').text.split(',')[0]
    except:
        declaration = 'no info'
    description = (soup.find('div', class_='foldable-description card-living-content__description').find('div', class_='text').text)
    values = [x.text.strip() for x in soup.find_all('span', class_='card-living-'
                                                        'content-params-list__value')]
    square, low_property, year, floors, material = values
    square = float(''.join([s for s in square.replace(',','.') if s.isdigit() or s == '.']))
    floor, all_floors = floors.split(' из ')
    telephone = soup.find('a', class_='offer-card-contacts-phones__phone')['href']

# переделать код ниже с помощью Selenium и Xpath чтобы уйти от проверок
    try:
        vendor = soup.find('a', class_='ui-kit-link offer-card-contacts__link _agency-name _type-common _color-blue').find('span', class_='ui-kit-link__inner').text.strip()
    except:
        vendor = 'undefinite vendor'
    try:
        agency = soup.find('a', class_='ui-kit-link offer-card-contacts__owner-name _type-common _color-blue').find('span', class_='ui-kit-link__inner').text.strip()
    except:
        agency = 'no agency'


    # print(f'{rooms = }\n{street = }\n{number = }\n{price = }\n{publish_date}\n{visits = }\n{declaration = }\n{description = }')
    # print(f'{square=}\n{low_property=}\n{year=}\n{floor=}\n{all_floors=}\n{material=}')
    # print(f'{vendor=}\n{agency=}\n{telephone=}')

    # Первая строка в выводе с заголовками
    flat_row = [rooms, street, number, square, floor, all_floors, price, publish_date, visits, declaration, description, low_property, year, material, agency, vendor, telephone]
    table.add_row(flat_row)
    print(table)
    return flat_row


print('\n', '----------------------------------------------', '\n', sep = '')
get_info(url)

# Обработка даты
def date_calculate():
    pass

