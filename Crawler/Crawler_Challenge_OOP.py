import csv
import time
from urllib.parse import urljoin
from crawler.ArticleFetcher import ArticleFetcher


site_base_url = "http://python.beispiel.programmierenlernen.io/"
site_index_url = "index.php"
page_fetcher = ArticleFetcher()
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
