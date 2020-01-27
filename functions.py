from urllib.request import urlopen

from util import *
import bs4 as BeautifulSoup

def getRandomWikiPage():
    html = urlopen("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard").read()
    soup = BeautifulSoup.BeautifulSoup(html, "html.parser")
    return soup

def getWikiPage(url):
    print("Trying to access " + url)
    html = urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html, "html.parser")
    return soup


def getPageTitle(soup):
    return soup.title.get_text().replace(" — Wikipédia", "")

def cleanSoup(soup):
    allLinks = []
    for div in soup.find_all("div",{"class":"bandeau-article"}):
        div.decompose()

    for div in soup.find_all("div",{"class":"homonymie"}):
        div.decompose()

    for div in soup.find_all("div",{"id":"toc", "class":"toc"}):
        div.decompose()

    for span in soup.find_all("span",{"class":"mw-editsection"}):
        span.decompose()

    for link in soup.find("div", {"id": "mw-content-text"}).find_all("a"):
        
        if link.get_text() != "":
            if link.get_text()[0] in "[?]":
                link.decompose()
            elif str(type(link.get('href'))) == "<class 'NoneType'>":
                link.decompose()
            elif link.get("href")[0] not in "/":
                link.decompose()
            else:
                allLinks.append((link.get_text(), link.get("href")))


    return allLinks

