#triangle.py
#Jackson Lambert
#Allows Users to draw a traingle
import math
from graphics import *
def main() :
    win = GraphWin("Triangle Calculator",500, 500)
    opening = Text(Point(200, 30), "Click any 3 points to draw a triangle").draw(win)
    p1 = win.getMouse()
    Circle(Point(p1.getX(),p1.getY()), 3).draw(win)
    p2 = win.getMouse()
    Circle(Point(p2.getX(), p2.getY()), 3).draw(win)
    p3 = win.getMouse()
    Circle(Point(p3.getX(), p3.getY()), 3).draw(win)
    triangle = Polygon(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()), Point(p3.getX(),p3.getY())).draw(win)
    dx1 = p1.getX() - p2.getX()
    dy1 = p1.getY() - p2.getY()
    dx2 = p2.getX() - p3.getX()
    dy2 = p2.getY() - p3.getY()
    dx3 = p3.getX() - p1.getX()
    dy3 = p3.getY() - p1.getX()
    a = float(math.sqrt((dx1**2 + dy1**2)))
    b = float(math.sqrt((dx2**2 + dy2**2)))
    c = float(math.sqrt((dx3**2 + dy3**2)))
    s = (a-b-c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    perm = a + b + c
    perm = round(perm, 2)
    area = round(area, 2)
    perm = str(perm)
    area = str(area)
    opening.undraw()
    Text(Point(200, 80), "The area is " + area + " " + "pixels").draw(win)
    Text(Point(200, 105), "The perimeter is " + perm + " " + "pixels").draw(win)
    Text(Point(200, 130), "Click Twice to exit").draw(win)
    win.getMouse()
    win.getMouse()
    win.close()
main()
