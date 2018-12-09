#archery.py
#Jackson Lambert 12-9-18
#Creates and archery targe

from graphics import *

def main() :
    win = GraphWin()
    #White Ring
    wCircle = Circle(Point(100,100), 50)
    wCircle.setFill("white")
    wCircle.draw(win)
    #Black Ring
    blaCircle = Circle(Point(100,100), 40)
    blaCircle.setFill("black")
    blaCircle.draw(win)
    #Blue Ring
    bluCircle = Circle(Point(100,100), 30)
    bluCircle.setFill("blue")
    bluCircle.draw(win)
    #Red Ring
    rCircle = Circle(Point(100,100), 20)
    rCircle.setFill("red")
    rCircle.draw(win)
    #Yellow Circle
    yCircle = Circle(Point(100,100), 10)
    yCircle.setFill("yellow")
    yCircle.draw(win)
    
main()
