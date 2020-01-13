import msvcrt as m
import os
from urllib.request import urlopen

import bs4 as BeautifulSoup


def clear(): return os.system('cls')


def wait():
    m.getch()


def getRandomWikiPage():
    html = urlopen(
        'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard').read()
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
    return soup


def getPageTitle(soup):
    return soup.title.get_text().replace(' — Wikipédia', '')


def mainMenu():
    token = True
    while token:
        clear()
        print("You are in Main menu.")
        print("1- Start a game")
        print("0- Exit")
        mainInput = input()
        if mainInput not in ["0", "1"]:
            clear()
            print("Invalid prompt!\nPress any key to continue")
            wait()


mainMenu()
