import requests
from bs4 import BeautifulSoup
class YoutubeScraper:
    def __init__(self, url):
        self.url = url
    def scrape_video_count(self):
        content = requests.get(self.url)
        soup = BeautifulSoup(content.text, "html.parser")
        view_count = soup.find("div", {"class": "watch-view-count"}).text
        return view_count

url = "https://www.youtube.com/watch?v=kix_vo3a5t4&list=PL0lO_mIqDDFUwVWvVitxG2oXA6a-Nq-Qq&index=11"
x = YoutubeScraper(url)
x.scrape_video_count()