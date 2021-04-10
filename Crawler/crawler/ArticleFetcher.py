
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .Article import Article
#.Article because they are in same directory

class ArticleFetcher():
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