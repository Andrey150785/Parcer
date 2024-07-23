from bs4 import BeautifulSoup
import requests
import json

URL_site = 'https://parsinger.ru/html/'

result_json = []
categories = []
article = []
name =[]
price = []
info = []
keys_info = []
links = []
old_price = []
count = []
link = []
page_links = []
li_id = ['categories', 'name', 'article', 'description', 'count', 'price', 'old_price', 'link']


for i in range(1, 6):
    for j in range(1, 5):
        url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        links.extend([x['href'] for x in soup.find_all('a', class_='name_item')])
        for x in range(8):
            categories.append([l['id'] for l in soup.find('div', class_='nav_menu').find_all('div')][i-1])


for L in links:
    URL = URL_site + L
    link.append(URL)
    response = requests.get(url=URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name.extend([x.text.strip() for x in soup.find_all('p', id='p_header')])
    article.extend([x.text.split(':')[1].strip() for x in soup.find_all('p', class_='article')])
    price.extend([x.text for x in soup.find_all('span', id='price')])
    old_price.extend([x.text for x in soup.find_all('span', id='old_price')])
    description = {i['id']: i.text.split(': ')[1].strip() for i in soup.find_all('li')}  # собираем бренд и тд.
    info.append(description)
    count.extend([x.text.split(':')[1].strip() for x in soup.find_all('span', id='in_stock')])



for c, n, a, d, cn, p, op, l in zip(categories, name, article, info, count, price, old_price, link):
    result_json.append({
        li_id[0] : c,
        li_id[1] : n,
        li_id[2] : a,
        li_id[3]: d,
        li_id[4] : cn,
        li_id[5] : p,
        li_id[6] : op,
        li_id[7] : l
    })

print(result_json)

with open('result5.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)