import requests
from bs4 import BeautifulSoup
import csv
import datetime
from time import perf_counter as pf
from get_card_info import get_info, url, columns

# print(get_info(url))
# print('\n', '----------------------------------------------', '\n', sep = '')

# Сохранить информацию в файл CSV
file_name = f'Flats on {datetime.date.today().isoformat()}, {pf():.2f}' #Уникальное название файла
print(file_name)

with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(columns)

with open(f'{file_name}.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(get_info(url))