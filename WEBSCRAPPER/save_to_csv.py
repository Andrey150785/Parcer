import requests
from bs4 import BeautifulSoup
import csv
import datetime
from time import perf_counter as pf
from get_card_info import get_info, url, columns
import sqlite3 as sq
<<<<<<< HEAD
=======

# print(get_info(url))
# print('\n', '----------------------------------------------', '\n', sep = '')
>>>>>>> 65b88aa8d6c82033871fe68eac3ad4672493941f

# Сохранить информацию в файл CSV
file_name = f'Flats on {datetime.date.today().isoformat()}, {pf():.2f}' #Уникальное название файла
print(file_name)

with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(columns)

with open(f'{file_name}.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(get_info(url))

<<<<<<< HEAD
# Сохранить информацию в БД SQLite
# with sq.connect(f'{file_name}.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT *")
#     print(cur.fetchmany(3))
=======
with sq.connect(f'{file_name}.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE score > 500 ORDER BY score DESC LIMIT 5")
    print(cursor.fetchmany(3))
>>>>>>> 65b88aa8d6c82033871fe68eac3ad4672493941f
