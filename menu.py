from util import *
from functions import *
exit = False

souplist = []


def mainMenu():
    token = True
    while token:
        clear()
        print("You are in Main menu.")
        print(c("1 ", "cyan") + "- Start a game")
        print(c("0 ", "cyan") + "- Exit")
        mainInput = input()
        if mainInput not in ["0", "1"]:
            clear()
            print("Invalid prompt!\nPress any key to continue")
            wait()
        else:
            token = False
        if mainInput == "0":
            clear()
        elif mainInput == "1":
            gameMenu(getRandomWikiPage(), getRandomWikiPage())


def gameMenu(soup, destination):
    if soup == destination:
        clear()
        print(c("\n\n\nBravo!! You won!\n\n\nPress any key to exit the game", "green"))
        wait()
    souplist.append(soup)
    if len(souplist) >=2:
        if souplist[-1]==souplist[-2]:
            souplist.pop()
    
    token = True
    start = page = numero = 0
    currentTitle = getPageTitle(soup)
    destinationTitle = getPageTitle(destination)
    allLinks = cleanSoup(soup)

    while token:
        numero = page*10
        clear()
        print("Turn: " + c(str(len(souplist)), "magenta") +
              ", Page: " + c(str(page+1), "magenta"))
        print("You are on " + c(currentTitle, 'green') +
              " and want to go to " + c(destinationTitle, 'green'))

        if len(souplist) > 1:
            print(c("*", "cyan")+" - Return to previous wiki page")
        print(c("-", "cyan")+" - Previous")

        last = start+10 if start+10 < len(allLinks) else len(allLinks)
        for i in range(start, last):
            numeroList = str(i%10) # get last digit of input
            numeroList = c(numeroList, "cyan")

            if str(allLinks[i][0]) != "":
                print(numeroList + " - " +
                      str(allLinks[i][0]))

        print(c("+", "cyan")+" - Next")

        inputGame = input()

        if inputGame not in ["-", "*", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            clear()
            print(c("\n\n\nNot in list, press any key to continue", "red"))
            wait()
            pass  # reload menu

        elif inputGame == "-":
            if page >= 1:
                start -= 10
                page -= 1
            else:
                clear()
                print(c("\n\n\nNo previous page, press any key to continue", "red"))
                wait()

        elif inputGame == "+":
            if page < len(allLinks)/10-1:
                start += 10
                page += 1
            else:
                clear()
                print(c("\n\n\nNo next page, press any key to continue", "red"))
                wait()

        elif inputGame == "*":
            if len(souplist)>1:
                souplist.pop()
            else:
                clear()
                print(c("\n\n\nNot in list, press any key to continue","red"))
                wait()
            soup = souplist[len(souplist)-1]
            token = False
            gameMenu(soup, destination)

        else:
            start = 0
            numero += int(inputGame)
            token = False
            gameMenu(getWikiPage("https://fr.wikipedia.org" +
                                 allLinks[numero][1]), destination)
            pass


if __name__ == "__main__":
    # mainMenu()
    gameMenu(getWikiPage("https://fr.wikipedia.org/wiki/Panama_(Iowa)"), getWikiPage("https://fr.wikipedia.org/wiki/Iowa")) # test with Iowa and Panama (Iowa)
    pass