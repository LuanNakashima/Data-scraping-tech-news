import sys
from .scraper import get_tech_news
from .analyzer.ratings import top_5_categories, top_5_news
from .analyzer.search_engine import search_by_category, search_by_date,\
        search_by_tag, search_by_title


# Requisito 12
def analyzer_menu():
    res = input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )

    case = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:"
        }

    res2 = res
    if res in case:
        res2 = input(case[res])

    case2 = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_tag,
        "4": search_by_category,
        "5": top_5_news,
        "6": top_5_categories
    }

    if res == "0":
        return case2[res](int(res2))
    elif res in ["1", "2", "3", "4"]:
        return case2[res](res2)
    elif res in ["5", "6"]:
        return case2[res]()
    elif res == "7":
        print("Encerrando script")
    else:
        print("Opção inválida", file=sys.stderr)

