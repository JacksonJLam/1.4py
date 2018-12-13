#rulermm.py
#Jackson Lambert 12-13-18
#creates a ruler with cm and in

from graphics import *

def main() :
    win = GraphWin("Ruler", 1200, 500)
    Rectangle(Point(10,300), Point(1160,200)).draw(win)
    for i in range(13) :
        Line(Point(10 + 95.83 * i, 200), Point(10 + 95.83 * i, 225)).draw(win)
        Text(Point(10+ 95.83 * i, 232), 0 + 1 * i).draw(win)
    for i in range(49) :
        Line(Point(10 + 23.95 * i, 200), Point(10 + 23.95 * i, 215)).draw(win)
    for i in range(31) :
        Line(Point(10 + 37.72 * i, 300), Point(10 + 37.72 * i, 280)).draw(win)
        Text(Point(10 + 37.72 * i, 275), 0 + 1 * i).draw(win)
    for i in range(301) :
        Line(Point(10 + 3.77 * i, 300), Point(10 + 3.77 * i, 290)).draw(win)
main()
