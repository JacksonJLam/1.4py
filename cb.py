#cb.py
#Jackson Lambert 12-12-18
#Creates a checkerboard pattern

from graphics import *

def main() :
    win = GraphWin("Checkerbaord", 802, 802)
    for i in range(4) :
        Rectangle(Point(0 + 200*i,0), Point(100 + 200 * i,100)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,0), Point(200 + 200 * i,100)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,100), Point(100 + 200 * i,200)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,100), Point(200 + 200 * i,200)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,200), Point(200 + 200 * i,300)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,200), Point(100 + 200 * i,300)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,300), Point(200 + 200 * i,400)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,300), Point(100 + 200 * i,400)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,400), Point(100 + 200 * i,500)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,400), Point(200 + 200 * i,500)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,500), Point(200 + 200 * i,600)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,500), Point(100 + 200 * i,600)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,600), Point(200 + 200 * i,700)).draw(win).setFill("black")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,600), Point(100 + 200 * i,700)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(100 + 200*i,700), Point(200 + 200 * i,800)).draw(win).setFill("red")
    for i in range(4) :
        Rectangle(Point(0 + 200*i,700), Point(100 + 200 * i,800)).draw(win).setFill("black")
main()
