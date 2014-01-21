from graphics import *

class window:

    def __init__(self, window):

        self.win = window

        # Set basic grid
        vLine = Line(Point(6, 12),Point(6,0))
        vLine.setWidth(3)
        vLine.draw(self.win)
        hLine = Line(Point(0, 2.5), Point(10, 2.5))
        hLine.setWidth(3)
        hLine.draw(self.win)

        # Inventory Rectangle
        invBox = Rectangle(Point(6.5, 3.5),Point(9.5, 10))
        invBox.setWidth(2)
        invBox.draw(self.win)
        # Line 1
        invLine = Line(Point(6.5, 8.375),Point(9.5, 8.375))
        invLine.setWidth(2)
        invLine.draw(self.win)
        # Line 2
        invLine2 = Line(Point(6.5, 6.75),Point(9.5, 6.75))
        invLine2.setWidth(2)
        invLine2.draw(self.win)
        # Line 3
        invLine3 = Line(Point(6.5, 5.125),Point(9.5, 5.125))
        invLine3.setWidth(2)
        invLine3.draw(self.win)
        # Line 4
        invLine4 = Line(Point(8, 3.5),Point(8, 10))
        invLine4.setWidth(2)
        invLine4.draw(self.win)
        # Inventory Text
        invText = Text(Point(8, 11), "INVENTORY")
        invText.setSize(20)
        invText.setStyle("bold")
        invText.draw(self.win)

        # HP
        self.hp = 100
        hpImage = Image(Point(.6, 1.75),"heart2.gif")
        hpImage.draw(self.win)
        self.hpAmt = Text(Point(1.5, 1.75), self.hp)
        self.hpAmt.draw(self.win)

        # MP
        self.mp = 100
        mpImage = Image(Point(.6, .5),"mana.gif")
        mpImage.draw(self.win)
        self.mpAmt = Text(Point(1.5, .5), self.mp)
        self.mpAmt.draw(self.win)

        # gold
        self.gold = 0
        goldImage = Image(Point(3.7, 1.15),"coin.gif")
        goldImage.draw(self.win)
        self.goldAmt = Text(Point(4.5, 1.15), self.gold)
        self.goldAmt.draw(self.win)

        # Inventory
        self.inventory = []
        self.hPot = 0
        self.mPot = 0
        self.tScroll = 0

        # Images
        self.keyImage = Image(Point(8.73, 7.575),"key.gif")
        self.teleImage = Image(Point(8.73, 5.95),"teleportscroll.gif")
        self.hpImage = Image(Point(7.25, 4.325),"HPpotion.gif")
        self.mpImage = Image(Point(8.73, 4.325),"MPpotion.gif")

        # Text
        self.hText = Text(Point(7.5, 4), self.hPot)
        self.mText = Text(Point(9, 4), self.mPot)


    def hp(self, number):
        self.hp = self.hp + number
        self.hpAmt.undraw()

        self.hpAmt = Text(Point(1.5, 1.75), self.hp)
        self.hpAmt.draw(self.win)

    def mp(self, number):
        self.mp = self.mp + number
        self.mpAmt.undraw()

        self.mpAmt = Text(Point(1.5, .5), self.mp)
        self.mpAmt.draw(self.win)

    def gold(self, number):
        if self.gold + number >= 0:
            self.gold = self.gold + number
            self.goldAmt.undraw()

            self.goldAmt = Text(Point(4.5, 1.15), self.gold)
            self.goldAmt.draw(self.win)
        else:
            print("Insufficient funds")

    def addInventory(self, item):
        self.inventory.append(item)
        if item == "begSword":
            begSwordImage = Image(Point(7.3, 9.2),"begsword.gif")
            begSwordImage.draw(self.win)
        elif item == "shield":
            shieldImage = Image(Point(8.8, 9.2),"shield.gif")
            shieldImage.draw(self.win)
        elif item == "robe":
            robeImage = Image(Point(7.25, 7.575),"robe.gif")
            robeImage.draw(self.win)
        elif item == "key":
            self.keyImage.draw(self.win)
        elif item == "tele":
            self.tScroll = self.tScroll + 1
            if self.tScroll == 1:
                self.teleImage.draw(self.win)
                self.tsText = Text(Point(9.25, 5.35), self.tScroll)
                self.tsText.draw(self.win)
            elif self.tScroll > 1:
                self.tsText.undraw()
                self.tsText = Text(Point(9.25, 5.35), self.tScroll)
                self.tsText.draw(self.win)

    def delInventory(self, item):
        self.inventory.remove(item)
        if item == "key":
            self.keyImage.undraw()
        if item == "tele":
            self.tsText.undraw()
            self.tScroll = self.tScroll - 1
            if self.tScroll == 0:
                self.teleImage.undraw()
                Rect = Rectangle(Point(6.5, 6.75), Point(8, 5.125))
                Rect.setFill('grey70')
                Rect.setWidth(2)
                Rect.draw(self.win)
            if self.tScroll >= 1:
                self.tsText.undraw()
                self.tsText = Text(Point(9.25, 5.35), self.tScroll)
                self.tsText.draw(self.win)

    def room1MiniMap(self):
        minimap = Rectangle(Point(7.25, .5), Point(8.75, 2))
        minimap.setWidth(2)
        minimap.draw(self.win)
        minimapLine = Line(Point(8, 2), Point(8, .5))
        minimapLine.setWidth(2)
        minimapLine.draw(self.win)
        minimapLine2 = Line(Point(7.25, 1.25), Point(8.75, 1.25))
        minimapLine2.setWidth(2)
        minimapLine2.draw(self.win)
    
