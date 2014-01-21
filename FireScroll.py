from graphics import *

class firescroll:

    def __init__(self, window):
        
        self.win = window

        # Image
        self.fireImage = Image(Point(7.25, 5.95),"firescroll.gif")

        # Amount of scrolls
        self.fScroll = 0

    def addInventory(self):
        
        self.fScroll = self.fScroll + 1
        
        if self.fScroll == 1:
            self.fireImage.draw(self.win)
            self.fsText = Text(Point(7.75, 5.35), self.fScroll)
            self.fsText.draw(self.win)
            
        elif self.fScroll > 1:
            self.fsText.undraw()
            self.fsText = Text(Point(7.75, 5.35), self.fScroll)
            self.fsText.draw(self.win)

    def delInventory(self):
        
        self.fsText.undraw()
        self.fScroll = self.fScroll - 1
        
        if self.fScroll == 0:
            self.fireImage.undraw()
            Rect = Rectangle(Point(6.5, 6.75), Point(8, 5.125))
            Rect.setFill('grey70')
            Rect.setWidth(2)
            Rect.draw(self.win)
            
        if self.fScroll >= 1:
            self.fsText.undraw()
            self.fsText = Text(Point(7.75, 5.35), self.fScroll)
            self.fsText.draw(self.win)
