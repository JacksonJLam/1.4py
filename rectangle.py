#rectangle.py
#Jackson Lambert
#Allows Users to draw a rectangle
import math
from graphics import *
def main() :
    win = GraphWin("Rectangle Calculator",500, 500)
    opening = Text(Point(200, 30), "Click Any Two Points To Create a Line").draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    rectangle = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY())).draw(win)
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    perm = length * 2 + width * 2
    area = length * width
    width = str(width)
    length = str(length)
    perm = str(perm)
    area = str(area)
    opening.undraw()
    Text(Point(200, 30), "The length is " + length + " " + "pixels").draw(win)
    Text(Point(200, 55), "The width is " + width + " " + "pixels").draw(win)
    Text(Point(200, 80), "The area is " + area + " " + "pixels").draw(win)
    Text(Point(200, 105), "The perimeter is " + perm + " " + "pixels").draw(win)
    Text(Point(200, 130), "Click Twice to exit").draw(win)
    win.getMouse()
    win.getMouse()
    win.close()
main()
