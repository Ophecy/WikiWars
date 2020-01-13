import bs4 as BeautifulSoup
from urllib.request import urlopen

def getRandomWikiPage():
    html = urlopen('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard').read()
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
    return soup