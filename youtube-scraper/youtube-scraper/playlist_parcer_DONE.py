from selenium import webdriver
from bs4 import BeautifulSoup as BS
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

URL = "https://www.youtube.com/watch?v=kix_vo3a5t4&list=PL0lO_mIqDDFUwVWvVitxG2oXA6a-Nq-Qq&index=11" #Ваш урл
links = []
result = dict()

options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

driver.get(URL)
time.sleep(8)  #Можно ждать до загрузки страницы, но проще подождать 10 секунд, их хватит с запасом
html = driver.page_source
soup = BS(html, "html.parser")


title = soup.find("a", {"class":"yt-simple-endpoint style-scope yt-formatted-string"}).text

videos = soup.find_all("ytd-playlist-panel-video-renderer",{"class":"style-scope ytd-playlist-panel-renderer"})
for video in videos:
    a = video.find("a",{"id":"wc-endpoint"})
    name = a.get_text()
    link = "https://www.youtube.com/" + a.get("href")
    links.append(link)

result[title] = links

print(result)
