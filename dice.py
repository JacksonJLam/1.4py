#dice.py
#draws dice 1-5
#Jackson Lambert 12-9-18
from graphics import *

def main() :
    win = GraphWin()
    i = 0
    for i in range(5) :
        move = 30 * i
    
        dice = Rectangle(Point(25,25), Point(50,50))
        dicecopy = dice.clone()
        dice.draw(win)
        dicecopy.move(move, 0)
        dicecopy.draw(win)

        dcenter = Circle(Point(37.5 + 30 *i ,37.5), 2)
        dcenter.draw(win)
        
        dbleft = Circle(Point(30 + move ,32.5), 2)
        dbright = Circle(Point(45 + move ,32.5), 2)
        tleft = Circle(Point(30 + 30 *i ,42.75), 2)
        tright = Circle(Point(45 + 30 *i ,42.75), 2)
        dbleft.draw(win)
        dbright.draw(win)
        tright.draw(win)
        tleft.draw(win)

        if i == 0 :
            dbleft.undraw()
            dbright.undraw()
            tleft.undraw()
            tright.undraw()
        if i == 1 :
            dcenter.undraw()
            tleft.undraw()
            dbright.undraw()
        if i == 2 :
            tright.undraw()
            dbleft.undraw()
            
        
        if i == 3 :
            dcenter.undraw()
    
main()
