#winter.py
#Jackson Lambert 12-9-18
#Draws a winter scene
from graphics import *
def main() :
    win = GraphWin()
    #Snowy background
    snow = Rectangle(Point(0, 50), Point(200,200))
    snow.setFill("white")
    snow.setOutline("white")
    #Sky
    sky = Rectangle(Point(0,50), Point(200,0))
    log = Rectangle(Point(40, 80), Point(60,100))
    sky.setFill("skyblue")
    sky.setOutline("skyblue")
    #Log of the Tree
    log.setFill("brown")
    log.setOutline("brown")
    #Tree Leaves
    treep1 = Polygon(Point(50,10),Point(25,40), Point(75, 40))
    treep1.setFill("green")
    treep1.setOutline("green")
    treep2 = Polygon(Point(50,20),Point(25,60), Point(75, 60))
    treep2.setFill("green")
    treep2.setOutline("green")
    treep3 = Polygon(Point(50,40),Point(25,80), Point(75, 80))
    treep3.setFill("green")
    treep3.setOutline("green")
    #Snow Man
    c1 = Circle(Point(150,150), 30)
    c1.setFill("white")
    c2 = Circle(Point(150, 125), 25)
    c2.setFill("white")
    c3 = Circle(Point(150, 90), 20)
    c3.setFill("white")
    i1 = Circle(Point(145, 80), 2.5)
    i1.setFill("black")
    i2 = Circle(Point(157, 80), 2.5)
    i2.setFill("black")
    n = Polygon(Point(150, 95), Point(150, 85), Point(175, 95))
    n.setFill("orange")
    b1 = Circle(Point(150, 120), 5)
    b1.setFill("black")
    b2 = Circle(Point(150, 140), 5)
    b2.setFill("black")
    #Draw Order
    snow.draw(win)
    sky.draw(win)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    i1.draw(win)
    i2.draw(win)
    n.draw(win)
    b1.draw(win)
    b2.draw(win)
    treep1.draw(win)
    treep2.draw(win)
    treep3.draw(win)
    log.draw(win)
    
main()
