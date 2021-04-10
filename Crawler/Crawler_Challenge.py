import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv


class Article():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image


class PageFetcher():
    def fetch(self, link):
        url = link
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        # articles = []
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            imageUrl = card.select_one("img").attrs["src"]
            image = urljoin(url, imageUrl)
            #instead of creating all at one, yield will create Article when needed
            yield Article(title, emoji, content, image)
            # articles.append(crawled)
        # return articles

    def next_url(self, link):
        url = link
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")
        if(doc.select(".navigation .btn.btn-primary")):
            return doc.select_one(".navigation .btn.btn-primary").attrs["href"]
        else:
            return ""


site_base_url = "http://python.beispiel.programmierenlernen.io/"
site_index_url = "index.php"
page_fetcher = PageFetcher()
hasNext = True
articles = []
while hasNext:
    url = urljoin(site_base_url, site_index_url)
    print("url:" + url)
    articles += (page_fetcher.fetch(url))
    print(articles[-1])
    time.sleep(1)
    site_index_url = page_fetcher.next_url(url)
    time.sleep(0.5)
    print("index_url: " + site_index_url)
    if("".__eq__(site_index_url)):
        hasNext = False
    else:
        hasNext = True


with open('crawler_article.csv', 'w', newline='',encoding="utf-8") as csvfile:
    article_writer = csv.writer(csvfile, delimiter=';', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

    for article in articles:
        article_writer.writerow(
            [article.emoji, article.title, article.image, article.content])
