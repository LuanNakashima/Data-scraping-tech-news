import requests
import time
from parsel import Selector
from rich import print as rprint

# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, headers={ "user-agent": "Fake user-agent" }, timeout=3)
        if response.status_code == 200:
            # return response.headers["Content-Type"]
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

# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
