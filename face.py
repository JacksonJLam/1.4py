#face.py
#Jackson Lambert 12-9-18
#Creates a face

from graphics import *

def main() :
    win = GraphWin()
    i1 = Circle(Point(50,50), 20)
    i1.setFill("white")
    i2 = Circle(Point(125,50), 20)
    i2.setFill("white")
    in1 = Circle(Point(50,50), 12)
    in1.setFill("brown")
    in2 = Circle(Point(125,50), 12)
    in2.setFill("brown")
    p1 = Circle(Point(50,50), 5)
    p1.setFill("black")
    p2 = Circle(Point(125,50), 5)
    p2.setFill("black")
    mouth = Oval(Point(50,75), Point(125, 100))
    mouth.setFill("black")
    i1.draw(win)
    i2.draw(win)
    in1.draw(win)
    in2.draw(win)
    p1.draw(win)
    p2.draw(win)
    mouth.draw(win)
main()
