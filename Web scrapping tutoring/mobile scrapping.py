import requests
import json
from bs4 import BeautifulSoup

phones_data = []
urls = (f"https://parsinger.ru/html/index2_page_{i}.html" for i in range(1, 5))

rs = requests.session()

for url in urls:
    response = rs.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    links = soup.select("a.name_item")
    for link in (f"https://parsinger.ru/html/{j['href']}" for j in links):
        card_response = rs.get(link)
        card_response.encoding = "utf-8"
        card_soup = BeautifulSoup(card_response.text, "lxml")

        phone_data = {
            "categories": "mobile",
            "name": card_soup.find(id="p_header").text.strip(),
            "article": card_soup.select_one("p.article").text.lstrip("Артикул: "),
        }

        phone_description = {}
        for li in card_soup.find(id="description").select("li"):
            _, info = li.text.split(": ")
            # print(info)
            phone_description[li["id"]] = info.strip()
            phone_data["description"] = phone_description
            phone_data["count"] = card_soup.find(id="in_stock").text.lstrip("В наличии: ")

        # for span in card_soup.select_one("div.sale").select("span"):
        #     phone_data[span["id"]] = span.text
        #
        # phone_data["link"] = link
        #
        # phones_data.append(phone_data)