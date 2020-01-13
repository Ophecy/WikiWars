from urllib.request import urlopen

from util import *
import bs4 as BeautifulSoup

exit = False
def getRandomWikiPage():
    html = urlopen(
        'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard').read()
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
    return soup


def getPageTitle(soup):
    return soup.title.get_text().replace(' — Wikipédia', '')