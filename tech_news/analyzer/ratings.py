from tech_news.database import find_news
# from rich import print as rprint


# Requisito 10
def top_5_news():
    db = find_news()
    newlist = sorted(db, key=lambda d: d['comments_count'], reverse=True)
    top_5 = []
    for news in newlist:
        top_5.append((news["title"], news["url"]))
    return top_5[:5]


# top_5_news()


# Requisito 11
def top_5_categories():
    db = find_news()
    db_category = [news["category"] for news in db]
    category_count = {news: db_category.count(news) for news in db_category}
    sorted_categories = sorted(
        sorted(list(category_count.items())), key=lambda category: (category[1]), reverse=True
    )
    top_5 =  [
        category
        for category, qnt in sorted_categories
    ]

    return top_5


top_5_categories()
