from graphics import *
from Window import window
from time import sleep
from FireScroll import firescroll

def main():

    # Create window
    win = GraphWin("Vault Breaker", 500, 600)
    win.setBackground('grey70')
    win.setCoords(0, 0, 10, 12)

    lol = window(win)
##    for i in range(10):
##    
##    num = eval(input("Enter number here: "))
    window.room1MiniMap(lol)

    time.sleep(2)
    firescroll.addInventory(lol)
    window.addInventory(lol, "tele")
    print("tele added: 1")

    time.sleep(2)
    firescroll.addInventory(lol)
    window.addInventory(lol, "tele")
    print("tele added: 2")

    time.sleep(2)
    firescroll.delInventory(lol)
    window.delInventory(lol, "tele")
    print("tele deleted: 1")

    time.sleep(2)
    firescroll.delInventory(lol)
    window.delInventory(lol, "tele")
    print("tele deleted: 0")


main()
