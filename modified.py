#Jackson Lambert
#Python Script Adjusted
#12-9-18
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getY()
        dy = p.getY() - c.getY()
        shapeCopy = shape.clone()
        shape.move(dx,dy)
        shapeCopy.draw(win)
    message = Text(Point(100,100),("Click anywhere to quit."))
    message.draw(win)
    win.getMouse() 
    win.close()

main()
        
