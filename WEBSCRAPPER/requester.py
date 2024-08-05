import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools
import lxml
import csv
from prettytable import PrettyTable

HOST = "https://novosibirsk.n1.ru/"
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10&rooms=1&is_newbuilding=false&total_area_min=30&total_area_max=50&release_date_min=2000&floor_not_first=true&floors_count_min=10"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def site_pagination(url):
    page_links = []
    page_links.append(url)
    for i in itertools.count(1):
        # Бесконечный цикл по карточкам товаров(часы).
        # Выбрать через Selenium 100 карточек на странице
        # для оптимизации запросов на сервер.
        URL_page = url + f'&page={i}'
        print(URL_page)
        try: # не работает проверка запроса ==200, так как он и так выполняется, но с пустым перечнем квартир
            response = requests.get(URL_page, headers=HEADERS) #, params=params)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            # if i < 5: #response.status_code == 200:
            #     page_links.append(URL_page)
                #get_content(URL_page)
            # else:
            #     break
            try:
                signal_element = soup.find('li', class_='paginator-pages__item _next')
            except:
                signal_element = None
            if signal_element is not None: #response.status_code == 200:
                page_links.append(URL_page)
            else:
                break
            # print(signal_element)
        except:
            print("Information blocked")
            break
    return page_links

# test
print(site_pagination(URL))

def get_content(html):
    response = requests.get(html, headers=HEADERS)  # , params=params)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all("div", class_="living-search-item offers-search__item")
    links_flats = []
    print(soup.find('title').text)
    # print(items)
    for item in items:
        # print(item.find('span', class_='link-text').get_text())
        link_href = item.find('a', class_='link')['href']
        links_flats.append(HOST+link_href)
    #print(links_flats)
    return links_flats

# Test
# print(get_content(URL))
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

for link_page in site_pagination(URL):
    flats_om_page =get_content(link_page) #ссылка на карточку по квартире
    for flat in flats_om_page: #получение подробной информации о квартире по ссылке выше
        print(flat)


#Тестирование get_info(https://novosibirsk.n1.ru//view/108334543/)
# get_info('https://novosibirsk.n1.ru//view/108334543/')