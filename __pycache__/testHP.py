from graphics import *
from Window import window


def main():

    # Create window
    win = GraphWin("Vault Breaker", 500, 600)
    win.setBackground('grey70')
    win.setCoords(0, 0, 10, 12)

    window(win)
##    for i in range(10):
##        lol = eval(input("What is the damage taken? "))
##        
##        window.hp(lol)

main()
