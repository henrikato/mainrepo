# Importa BeautifulSoup do pacote bs4 usando-o com o alias 'bs'
from bs4 import BeautifulSoup as bs
# Importa o pacote 'requests'
import requests

# Usa o pacote 'requests' para fazer uma requisição GET na página da URL
page = requests.get("http://en.wikipedia.org/wiki/Hurricane_Florence")
# Faz a mágica do BeautifulSoup no conteúdo da página acima, utilizando o parser 'html.parser'
soup = bs(page.content, 'html.parser')

# Buscar tudo que tenha a class 'mw-headline'
elementos = soup.find_all(class_="mw-headline")
for elemento in elementos:
    print(elemento)