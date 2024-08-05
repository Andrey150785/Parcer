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

def site_pagination(url):
    # ВЫДАЕТ СПИСОК ССЫЛОК НА СТРАНИЦЫ С ОБЪЯВЛЕНИЯМИ
    page_links = []
    page_links.append(url)
    for i in itertools.count(1):
        # Бесконечный цикл по карточкам товаров(часы).
        # Выбрать через Selenium 100 карточек на странице
        # для оптимизации запросов на сервер.
        URL_page = url + f'&page={i}'
        # print(URL_page)
        # не работает проверка запроса ==200, так как он и так выполняется, но с пустым перечнем квартир
        response = requests.get(URL_page, headers=HEADERS) #, params=params)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            signal_element = soup.find('li', class_='paginator-pages__item _next')
        except:
            signal_element = None
        if signal_element is not None:  # response.status_code == 200:
            page_links.append(URL_page)
        else:
            page_links.append(URL_page)
            break
        # except:
        #     print("Information blocked")
        #     break
    return page_links

# test
print(site_pagination(URL))
