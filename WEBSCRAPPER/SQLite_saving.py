import requests
from bs4 import BeautifulSoup
import datetime
from time import perf_counter as pf
import sqlite3 as sq
from prettytable import PrettyTable
from get_card_info import result

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
      'Продавец', 'Телефон', 'Ссылка']

table = PrettyTable() #Создаем таблицу для красивого вывода в консоль
table.field_names = columns

# Заменить текущую строку контекстного менеджера на ту, которая закоментирована
# with sq.connect(f'{file_name}.db') as conn:
with sq.connect(f'data.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS flats ( 
        Количество_комнат INTEGER, 
        Улица TEXT, 
        №_дома TEXT, 
        Площадь INTEGER, 
        Этаж INTEGER, 
        Этажей_в_доме INTEGER, 
        Цена INTEGER, 
        Дата_публикации TEXT,
        Количество_просмотров INTEGER, 
        Декларация TEXT, 
        Описание TEXT, 
        Собственность TEXT, 
        Год_постройки TEXT, 
        Материал_стен TEXT, 
        Агентство TEXT,
        Продавец TEXT, 
        Телефон TEXT, 
        Ссылка TEXT
        )""")

    r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17 = result
    # print(r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, sep = '\n')
    # print(f"INSERT INTO flats VALUES('0', {r0}, {r1}, {r2}, {r3}, {r4}, {r5}, {r6}, {r7}, {r8}, {r9}, {r10}, {r11}, {r12}, {r13}, {r14}, {r15}, {r16}, {r17})")
    cursor.execute(f"INSERT INTO flats VALUES('0', {r0}, {r1}, {r2}, {r3}, {r4}, {r5}, {r6}, {r7}, {r8}, {r9}, {r10}, {r11}, {r12}, {r13}, {r14}, {r15}, {r16}, {r17})")
    cursor.execute("""SELECT * FROM flats""")
    # print(cursor.fetchall())

