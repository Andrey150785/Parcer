import requests
from bs4 import BeautifulSoup
import datetime
from typing import Tuple, Any
from time import perf_counter as pf
from prettytable import PrettyTable
import lxml

HOST = "https://novosibirsk.n1.ru/"
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10&rooms=1&is_newbuilding=false&total_area_min=30&total_area_max=50&release_date_min=2000&floor_not_first=true&floors_count_min=10"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
url = 'https://novosibirsk.n1.ru/view/107311697/'


def get_info_N1(url):
    # функция, собирающая информацию из карточки объявления о квартире
    link = url
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    # Searching for elements:
    # 1. Headline parcing:
    rooms = [int(x) for x in soup.find('span', class_='deal-title').text if x.isdigit()][0]
    street = (soup.find('span', class_='address').text).strip(', ')
    number = (soup.find('span', class_='house-number').text).strip(', ')
    price = int(''.join([x for x in (soup.find('span', class_='price').text).strip(' ') if x.isdigit()]))

    # 2. Publish & statistic block:
    publish_date = (soup.select_one("div[class='trigger'] div").text).strip()  # дату нужно еще постараться вытянуть
    refresh_date = [x.text.strip() for x in soup.find('div', class_='meta').find_all('span', class_='label')][
        0]  # дату нужно еще постараться вытянуть
    try:
        visits = [x.text.strip() for x in soup.find('div', class_='meta').find_all('span', class_='label')][1]
    except:
        visits = 'no info'

    # 3. Description block:
    description = (soup.find('div', class_='foldable-description card-living-content__description').find('div',
                                                                                                         class_='text').text)
    try:
        declaration = soup.find('p', class_='card-living-content-declaration').text.split(',')[0]
    except:
        declaration = 'no info'

    # 4. Block of flat's parameters:
    values = [x.text.strip() for x in soup.find_all('span', class_='card-living-'
                                                                   'content-params-list__value')]
    square, *other, year, floors, material = values
    square = float(''.join([s for s in square.replace(',', '.') if s.isdigit() or s == '.']))
    floor, all_floors = floors.split(' из ')

    # 5. Contact's block:
    telephone = soup.find('a', class_='offer-card-contacts-phones__phone')['href']
    try:
        vendor = soup.find('a',
                           class_='ui-kit-link offer-card-contacts__link _agency-name _type-common _color-blue').find(
            'span', class_='ui-kit-link__inner').text.strip()
    except:
        vendor = 'undefinite vendor'
    try:
        agency = soup.find('a', class_='ui-kit-link offer-card-contacts__owner-name _type-common _color-blue').find(
            'span', class_='ui-kit-link__inner').text.strip()
    except:
        agency = 'no agency'

    # 6. Flatrow done in list-form:
    flat_row = [rooms, street, number, square, floor, all_floors, price, publish_date, visits, declaration, description,
                year, material, agency, vendor, telephone, link]

    return flat_row


# # Show table in console
# file_name = f'Flats on {datetime.date.today().isoformat()}, {pf():.2f}'  # Уникальное название файла
# table = PrettyTable()  # Создаем таблицу для красивого вывода в консоль
#
# # Первая строка в выводе с заголовками. Вывод красивой таблицы в консоль
# columns = ['Количество комнат', 'Улица', '№ дома', 'Площадь', 'Этаж', 'Этажей в доме', 'Цена', 'Дата публикации',
#            'Количество просмотров', 'Декларация', 'Описание', 'Год постройки', 'Материал стен',
#            'Агентство',
#            'Продавец', 'Телефон', 'Ссылка']
# table.field_names = columns
# table.add_row(get_info_N1(url))
# print(table)


# Обработка даты
def date_calculate(dt:str)-> tuple[str | Any, str | Any]:
    year = None
    month = None
    day = None
    today = datetime.date.today()
    datestring = dt.split()
    datestring.append('2024')
    date_dict = {'сегодня':today, 'вчера': today-datetime.timedelta(days=1)}
    month_dict = {
        'янв': '01',
        'фев': '02',
        'мар': '03',
        'апр': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'авг': '08',
        'сен': '09',
        'окт': '10',
        'ноя': '11',
        'дек': '12'
    }
    if dt in ['сегодня', 'вчера']:
        DT = date_dict[dt]
        print(DT)
    else:
        datestring[1] = month_dict[datestring[1]]
        DT = datetime.date.fromisoformat('-'.join(datestring[::-1]))
        print(DT)
    delta = abs(today - DT)
    return str(DT), str(delta)

    # link = url
    # response = requests.get(url, headers=HEADERS)
    # soup = BeautifulSoup(response.text, 'lxml')
    # publish_date = (soup.select_one("div[class='trigger'] div").text).strip()  # дату нужно еще постараться вытянуть
    # refresh_date = [x.text.strip() for x in soup.find('div', class_='meta').find_all('span', class_='label')][
    #     0]  # дату нужно еще постараться вытянуть
    # return publish_date, refresh_date

def searching_doubles():
    pass
