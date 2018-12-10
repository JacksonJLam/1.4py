#lineseg.py
#Jackson Lambert
#Allows Users to graw a line segment
import math
from graphics import *
def main() :
    win = GraphWin("Line Segment",500, 500)
    Text(Point(200, 30), "Click Any Two Points To Create a Line").draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    length= float(math.sqrt((p1.getX()-p2.getX())**2 + (p1.getY()-p2.getY())**2))
    middle = float(length/2)
    xmid = math.sqrt(float((p2.getX() + p1.getX())**2))/2
    ymid = math.sqrt(float((p2.getY() + p1.getY())**2))/2
    midpoint = Circle(Point(xmid, ymid), 2)
    midpoint.setFill("cyan")
    midpoint.draw(win)
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = dy / dx * -1
    length = str(length)
    slope = str(slope)
    Text(Point(200, 50), "The length Is " + length + " " + "pixels" ).draw(win)
    Text(Point(200, 75), "The Slope is " + slope).draw(win)
    Text(Point(200, 100), "Click Twice to exit ").draw(win)
    win.getMouse()
    win.getMouse()
    win.close()
main()
