import requests
from bs4 import BeautifulSoup
import lxml
import csv

# Constants
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
            "price": item.find('div', class_='living-list-card-price__item _object'),
            "status": item.find('span', class_='living-list-card-newbuilding__title'),
            "area": item.find('div',
                              class_='living-list-card__area living-list-card-area living-list-card__inner-block').get_text(),
            "phone": item.find('span', class_='common-list-item-phone__text').get_text(),
            "comments": item.find('div',
                                  class_='living-list-card__inner-block living-list-card__description').get_text(),
            "adlink": HOST + item.find("a", class_= "link").get('href')
        })
    return flats


responce = requests.get(URL)
dictionary = get_content(responce)
for item in dictionary:
    print(item)

def site_parser():
    html = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print('Error of getting site information')
