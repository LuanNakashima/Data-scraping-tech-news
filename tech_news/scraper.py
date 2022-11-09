import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from rich import print as rprint

# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, headers={ "user-agent": "Fake user-agent" }, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except:
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

def my_fetch():
    response = requests.get("https://blog.betrybe.com/", headers={ "user-agent": "Fake user-agent" })
    if response.status_code == 200:
        selector = Selector(text=response.text)
        article = selector.css("article.entry-preview").get()
        # return response.headers["Content-Type"]
        return article
    return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel*=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().replace(u'\xa0', u'').strip()
    date = selector.css(".meta-date::text").get()
    writer = selector.css("a.url::text").get()
    comments_count = len(selector.css(".comment-list li").getall())
    summary_html = selector.css(".entry-content p").get()
    sopinha_de_letrinhas = BeautifulSoup(summary_html, features="lxml").get_text().replace(u'\xa0', u'').strip()
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
    """Seu código deve vir aqui"""
