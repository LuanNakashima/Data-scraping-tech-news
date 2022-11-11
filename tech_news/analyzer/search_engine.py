from tech_news.database import search_news
from datetime import datetime
# from rich import print as rprint


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    db = search_news(query)
    news_title = []
    for news in db:
        news_title.append((news["title"], news["url"]))
    return(news_title)


# rprint(search_by_title("Notícia bacana"))


# Requisito 7
def search_by_date(date):
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").strftime('%d/%m/%Y')
        query = {"timestamp": new_date}
        db = search_news(query)
        news_date = []
        for news in db:
            news_date.append((news["title"], news["url"]))
        return(news_date)
    except ValueError:
        raise ValueError("Data inválida")


# rprint(search_by_date("2021/04/04"))

# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    db = search_news(query)
    news_tag = []
    for news in db:
        news_tag.append((news["title"], news["url"]))
    return(news_tag)


# rprint(search_by_tag("Tecnologia"))


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    db = search_news(query)
    news_category = []
    for news in db:
        news_category.append((news["title"], news["url"]))
    return(news_category)
