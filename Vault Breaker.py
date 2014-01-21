# Vault Breaker.py

from graphics import *

from Window import window

def main():
    
    # Create window
    win = GraphWin("Vault Breaker", 500, 600)
    win.setBackground('grey70')
    win.setCoords(0, 0, 10, 12)

    # Orc enemy
    orchp = 10
    orcImage = Image(Point(3, 8),"orc.gif")
    orcImage.draw(win)
    orcName = Text(Point(3, 4), "WARRIOR ORC Lv.40")
    orcName.setSize(15)
    orcName.setStyle("bold")
    orcName.draw(win)
    orcHPText = Text(Point(2.75, 3), "HP:")
    orcHPText.setFill("red")
    orcHPText.setStyle("bold")
    orcHPText.draw(win)
    orcHPCounter = Text(Point(3.5, 3), orchp)
    orcHPCounter.draw(win)

    tl(win, inventory)


def tl(win, inventory):

    tlCirc = Circle(Point(7.625 ,1.625), .3)
    tlCirc.setFill('red')
    tlCirc.draw(win)

    direction = input("Which direction?: ")

    if direction == "east":
        tlCirc.undraw()
        tr(win, inventory)
    elif direction == "south":
        tlCirc.undraw()
        bl(win, inventory)
    elif direction == "key":
        if "key" in inventory:
            inventory.remove("key")
            keyCirc = Circle(Point(8.73, 7.575), .65)
            keyCirc.setFill('grey70')
            keyCirc.setOutline('grey70')
            keyCirc.draw(win)
            print("\nYOU WIN!")
        else:
            print("\nYou aint got no key!\n")
            tlCirc.undraw()
            tl(win, inventory)
    else:
        tlCirc.undraw()
        tl(win, inventory)

def tr(win, inventory):

    trCirc = Circle(Point(8.375 ,1.625), .3)
    trCirc.setFill('red')
    trCirc.draw(win)

    direction = input("Which direction?: ")

    if direction == "west":
        trCirc.undraw()
        tl(win, inventory)
    elif direction == "south":
        trCirc.undraw()
        br(win, inventory)
    else:
        trCirc.undraw()
        tr(win, inventory)

def bl(win, inventory):

    blCirc = Circle(Point(7.625, .875), .3)
    blCirc.setFill('red')
    blCirc.draw(win)

    direction = input("Which direction?: ")

    if direction == "east":
        blCirc.undraw()
        br(win, inventory)
    elif direction == "north":
        blCirc.undraw()
        tl(win, inventory)
    else:
        blCirc.undraw()
        bl(win, inventory)

def br(win, inventory):

    brCirc = Circle(Point(8.375 ,.875), .3)
    brCirc.setFill('red')
    brCirc.draw(win)

    direction = input("Which direction?: ")

    if direction == "north":
        brCirc.undraw()
        tr(win, inventory)
    elif direction == "west":
        brCirc.undraw()
        bl(win, inventory)
    elif direction == "key":
        keyImage = Image(Point(8.73, 7.575),"key.gif")
        keyImage.draw(win)
        print ("\nKey added to inventory\n")
        inventory.append("key")
        brCirc.undraw()
        br(win, inventory)
    elif direction == "inventory":
        print("INVENTORY", inventory)
        brCirc.undraw()
        br(win, inventory)
    else:
        brCirc.undraw()
        br(win, inventory)

main()
