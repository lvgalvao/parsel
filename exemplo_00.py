from parsel import Selector
from httpx import get

html = """
<html>
    <head>
        <title>Título da página</title>
    </head>
    <body>
        <p> Boas vindas a minha página! </p>
    </body>
</html>
"""

# response = get('full_site.html').content.decode('utf-8')

sel = Selector(
    text=open('full_site.html', 'r', encoding='utf-8').read()
)   # cria uma instância do Selector e qual texto será analisado

# print(sel.css('h1').get())   # retorna o primeiro elemento encontrado
