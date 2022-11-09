import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from rich import print as rprint
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )
        response.raise_for_status()
        return response.text
    except(requests.HTTPError, requests.ReadTimeout):
        return None


# rprint(fetch("https://blog.betrybe.com/"))

# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(".entry-title a::attr(href)").getall()


# rprint(scrape_novidades(fetch("https://blog.betrybe.com/")))

# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# rprint(scrape_next_page_link(fetch("https://blog.betrybe.com/")))


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel*=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get()\
        .replace(u'\xa0', u'').strip()
    date = selector.css(".meta-date::text").get()
    writer = selector.css("a.url::text").get()
    comments_count = len(selector.css(".comment-list li").getall())
    summary_html = selector.css(".entry-content p").get()
    sopinha_de_letrinhas = BeautifulSoup(summary_html, features="lxml")\
        .get_text().replace(u'\xa0', u'').strip()
    summary = sopinha_de_letrinhas
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()
    news_data = {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return news_data


# rprint(scrape_noticia(fetch("https://blog.betrybe.com/carreira/fazer-curriculo-no-word-em-pdf/")))

# Requisito 5
def get_tech_news(amount):
    response = fetch("https://blog.betrybe.com/")
    url_news = scrape_novidades(response)
    all_news = []
    # all_news = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    for news in url_news:
        data_news = scrape_noticia(fetch(news))
        all_news.append(data_news)
    n = 1
    while len(all_news) < amount:
        n += 1
        next_url = "https://blog.betrybe.com/" + f"page/{n}/"
        url_news = scrape_novidades(fetch(next_url))
        # url_news = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
        new_index = amount - len(all_news)
        if new_index < 12:
            for i in range(new_index):
                data_news = scrape_noticia(fetch(url_news[i]))
                all_news.append(data_news)
        else:
            new_index = amount - 12
            for i in range(12):
                data_news = scrape_noticia(fetch(url_news[i]))
                all_news.append(data_news)
    create_news(all_news[:amount])
    return all_news[:amount]


# rprint(get_tech_news(30))
