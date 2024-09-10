from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time

URL = "https://www.youtube.com/watch?v=kix_vo3a5t4&list=PL0lO_mIqDDFUwVWvVitxG2oXA6a-Nq-Qq&index=11" #Ваш урл

driver = webdriver.Chrome()
driver.get(URL)
time.sleep(5)  #Можно ждать до загрузки страницы, но проще подождать 10 секунд, их хватит с запасом
html = driver.page_source
soup = BS(html, "html.parser")
videos = soup.find_all("ytd-playlist-panel-video-renderer",{"class":"style-scope ytd-playlist-panel-renderer"})
for video in videos:
    a = video.find("a",{"id":"wc-endpoint"})
    name = a.get_text()
    link = "https://www.youtube.com/" + a.get("href")
    print(name, link)
    # break