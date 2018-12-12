#5CH.py
#Jackson Lambert 12-12-18
#Allows Users to draw a house in 5 clicks
import math
from graphics import *
def main() :
    #Establish window
    win = GraphWin("5 Click House", 500, 500)
    #Window Greetings
    opening1 = Text(Point(250,100), "Welcome to the 5 click house generator").draw(win)
    opening2 = Text(Point(250,150), "Click twice anywhere to begin").draw(win)
    #Get input
    win.getMouse()
    win.getMouse()
    #Gets rid of openings
    opening1.undraw()
    opening2.undraw()
    #Tells the user to click
    click1txt = Text(Point(250,100), "Click Anywhere to select the first corner of the house").draw(win)
    p1 = win.getMouse()
    #Draws point where you click
    Circle(Point(p1.getX(),p1.getY()), 3).draw(win).setFill("red")
    ident1 = Text(Point(p1.getX(), p1.getY() - 20), "P1").draw(win)
    ident1.setSize(8)
    click1txt.undraw()
    #Second corner of the house
    click2txt = Text(Point(250,100), "Click Anywhere to select the second corner of the house").draw(win)
    p2 = win.getMouse()
    Circle(Point(p2.getX(),p2.getY()), 3).draw(win).setFill("blue")
    ident2 = Text(Point(p2.getX(), p2.getY() + 20), "P2").draw(win)
    ident2.setSize(8)
    click2txt.undraw()
    house = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY())).draw(win)
    house.setFill("purple")
    ident1.undraw()
    ident2.undraw()
    #Doorway
    centerPoint = house.getCenter
    click3txt = Text(Point(250, 100), "Click somewhere inside the house to select").draw(win)
    click3txt2 = Text(Point(250,125), "The doorway position").draw(win)
    p3 = win.getMouse()
    if p1.getY() > p2.getY() :
        bottomdw = p1.getY()
    if p2.getY() > p1.getY() :
        bottomdw = p2.getY()
    length = abs(p1.getX() - p2.getX())
    dwr = p3.getX() - length / 10
    dwl = p3.getX() + length / 10
    doorway = Rectangle(Point(dwr, bottomdw), Point(dwl, house.getCenter().getY())).draw(win).setFill("red")
    click3txt.undraw()
    click3txt2.undraw()
    #Window
    click4txt = Text(Point(250, 100), "Click somewhere inside the house to select a").draw(win)
    click4txt2 = Text(Point(250,125), "The window position").draw(win)
    p4 = win.getMouse()
    #Getting window points
    crn1x = p4.getX() - length /20
    crn1y = p4.getY() - length /20
    crn2x = p4.getX() + length /20
    crn2y = p4.getY() + length /20
    window = Rectangle(Point(crn1x, crn1y), Point(crn2x, crn2y)).draw(win).setFill("blue")
    click4txt.undraw()
    click4txt2.undraw()
    click5txt = Text(Point(250, 100), "Click somewhere above the house to select a").draw(win)
    click5txt2 = Text(Point(250,125), "The center of the roof's position").draw(win)
    #If statements so the triangle orients correctly
    p4 = win.getMouse()
    if p1.getY() < p2.getY() :
        triangle = Polygon(Point(p4.getX(), p4.getY()),Point(p2.getX(), p1.getY()), Point(p1.getX(), p1.getY())).draw(win).setFill("purple")
    if p2.getY() < p1.getY() :
        triangle = Polygon(Point(p4.getX(), p4.getY()),Point(p2.getX(), p2.getY()), Point(p1.getX(), p2.getY())).draw(win)
    click5txt.undraw()
    click5txt2.undraw()
    Text(Point(250, 100), "Here's the final product").draw(win)
    Text(Point(250, 125), "Click twice to exit").draw(win)
    win.getMouse()
    win.getMouse()
    win.close()
main()   
