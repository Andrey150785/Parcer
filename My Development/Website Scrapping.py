import requests
from bs4 import BeautifulSoup
import lxml
import csv

# Constants
CSV = 'cards.csv'
HOST = "https://novosibirsk.n1.ru/"
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


# Codes & Function
def get_html(url, params=''):
    responce = requests.get(url, headers=HEADERS, params=params)
    return responce


def get_content(html):
    soup = BeautifulSoup(html.text, 'lxml')
    items = soup.find_all("div", class_="living-list-card__col _main")
    flats = []
    print(soup.find('title').text)

    for item in items:
        flats.append(
        {
            "title": item.find('span', class_='link-text').get_text(),
            "grade": item.find('span', class_='living-list-card-floor__item').get_text(),
            "price": item.find('span', class_='price__value'),
            "status": item.find('span', class_='living-list-card-newbuilding__title'),
            "area": item.find('div',
                              class_='living-list-card__area living-list-card-area living-list-card__inner-block').get_text(),
            "phone": item.find('span', class_='common-list-item-phone__text').get_text(),
            "comments": item.find('div',
                                  class_='living-list-card__inner-block living-list-card__description').get_text(),
            "advertlink": HOST + item.find("a", class_= "link").get('href')
        })
    return flats

#Сохранение информации из cards в файл csv
def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Квартира','Этаж','Цена','Статус','Площадь','Телефон','Описание','Ссылка на объявление'])
        for item in items:
            writer.writerow(
                [item["title"], item["grade"], item["price"], item["status"], item["area"], item["phone"], item["comments"], item["advertlink"]])
def site_parser():
    PAGENATION = int(input('Укажите количество страниц для парсинга: ').strip())
    html = get_html(URL) #Проерка работы запроса и получение ответа 200 с дальнейшим условием обработки
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION+1):
            print(f'Processing page {page}')
            html = get_html(URL, params = {'page':page})
            cards.extend(get_content(html))
            save_doc(cards, CSV)
        print('Parsing finished')

        print()
        print(*[i for i in cards], sep = "\n")

    else:
        print('Error of getting site information')


site_parser()