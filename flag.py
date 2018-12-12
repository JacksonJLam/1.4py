#flag.py
#Jackson Lambert
#draws the frenh flag

from graphics import *

def main() :
    win = GraphWin("Flag", 900, 600)
    b = Rectangle(Point(0,0), Point(300,599)).draw(win)
    w = Rectangle(Point(300,599), Point(600,0)).draw(win).setOutline("white")
    r = Rectangle(Point(600,0), Point(898,599)).draw(win)
    b.setOutline("navyblue")
    b.setFill("navyblue")
    r.setFill("red")
    r.setOutline("red")
    

main()
