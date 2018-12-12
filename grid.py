#graph.py
#Jackson Lambert 12-12-18
#Makes a standard 4 quadrant grid
from graphics import *

def main() :
    win = GraphWin("Grid", 505,505)
    yaxis = Line(Point(250, 500), Point(250, 0))
    xaxis = Line(Point(500, 250), Point(0,250))
    xaxis.draw(win)
    yaxis.draw(win)
    i = 0
    for i in range(11) :
        tickx = Line(Point(i*50, 260), Point(i*50, 240))
        tickx.draw(win)
        ticky = Line(Point(260, i*50), Point(240, i*50))
        ticky.draw(win)
main()
