import requests
from bs4 import BeautifulSoup
import datetime
from time import perf_counter as pf
import sqlite3 as sq
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

# SQL & csv saving attributes. Сохранить информацию в базу данных SQLite и файл CSV:

file_name = f'Flats on {datetime.date.today().isoformat()}, {pf():.2f}' #Уникальное название файла
columns = ['Количество комнат', 'Улица', '№ дома', 'Площадь', 'Этаж', 'Этажей в доме', 'Цена', 'Дата публикации',
      'Количество просмотров', 'Декларация', 'Описание', 'Собственность', 'Год постройки', 'Материал стен', 'Агентство',
      'Продавец', 'Телефон']

table = PrettyTable() #Создаем таблицу для красивого вывода в консоль
table.field_names = columns

with sq.connect(f'{file_name}.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE flats (id INTEGER PRIMARY KEY, name TEXT)')
    print(cursor.fetchmany(3))