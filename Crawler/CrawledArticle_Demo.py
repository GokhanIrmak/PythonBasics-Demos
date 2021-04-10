import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image


class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            imageUrl = card.select_one("img").attrs["src"]
            image = urljoin(url,imageUrl)
            crawled = CrawledArticle(title, emoji, content, image)
            articles.append(crawled)

        return articles

# print(r.status_code)
# print(r.headers)
# print(r.text)


# for p in doc.find_all("p"):
#     print(p.text)
#     print(p.attrs) #Print attributes of 'p'

# Selecting with CSS Selectors
# cards = doc.select(".card")
# print(cards)

# emojis = doc.select(".emoji")
# print(emojis)



fetcher = ArticleFetcher()
fetched = fetcher.fetch()[0]
print(fetched.image)
