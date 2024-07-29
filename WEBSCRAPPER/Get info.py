import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools
import lxml
import csv

HOST = "https://novosibirsk.n1.ru/"
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10&rooms=1&is_newbuilding=false&total_area_min=30&total_area_max=50&release_date_min=2000&floor_not_first=true&floors_count_min=10"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def get_info(url):
    # функция, собирающая информацию из карточки объявления о квартире
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    print(*[int(x) for x in soup.find('span', class_='deal-title').text if x.isdigit()]) #проверка на цифры(soup.find('span', class_='deal-title').text))
    print((soup.find('span', class_='address').text).strip(', '))
    print((soup.find('span', class_='house-number').text).strip(', '))
    print(int(''.join([x for x in (soup.find('span', class_='price').text).strip(' ') if x.isdigit()])))
    print([x.text for x in soup.find('div', class_='meta').find_all('span', class_='label')]) # дату нужно еще постараться вытянуть
    print(soup.find('p', class_='card-living-content-declaration').text.split(',')[0])
    print(soup.find('div', class_='foldable-description card-living-content__description').find('div', class_='text').text)
    print([x.text for x in soup.find_all('span', class_='card-living-'
                                                        'content-params-list__value')])
    # переделать код ниже с помощью Selenium и Xpath чтобы уйти от проверок
    try:
        print(soup.find('a', class_='ui-kit-link offer-card-contacts__link _agency-name _type-common _color-blue').find('span', class_='ui-kit-link__inner').text.strip())
    except:
        pass
    try:
        print(soup.find('a', class_='ui-kit-link offer-card-contacts__owner-name _type-common _color-blue').find('span', class_='ui-kit-link__inner').text.strip())
    except:
        pass

    print(soup.find('a', class_='offer-card-contacts-phones__phone')['href'])
    print('\n', '----------------------------------------------', '\n', sep = '')