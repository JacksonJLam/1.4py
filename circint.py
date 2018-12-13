#circint.py
#Jackson Lambert 12-10-18
#Creates a circle and
from graphics import *
import math

def main() :
    win = GraphWin("Circle Window", 400, 400)
    
    inputs = GraphWin("Input Window", 400,400)
   
    Text(Point(200,75),"Y Intercept").draw(inputs)
    Text(Point(200,125),"Circle Radius").draw(inputs)
    input1 = Entry(Point(200,150), 20)
    input2 = Entry(Point(200,100), 20)
    input1.draw(inputs)
    input2.draw(inputs)
    calc = Text(Point(200,175), "Click Here To Draw Your Circle")
    calc.draw(inputs)
    inputs.getMouse()
    inputs.close()
    radius= float(input1.getText())
    intercept= float(input2.getText())
    Circle(Point(0,0), radius).draw(win)
    Line(Point(-10, intercept), Point(10, intercept)).draw(win).setOutline("blue")
    win.setCoords(-10, -10, 10, 10)
    xint = math.sqrt((radius**2) - (intercept**2))
    Circle(Point(xint, intercept),.25).draw(win).setFill("red")
    Circle(Point(-1 * xint, intercept),.25).draw(win).setFill("red")
    xint = str(xint)
    printxint = "-/+" + xint
    Text(Point(3,9), "The X intercepts of the line & circles are").draw(win)
    Text(Point(5,8), printxint).draw(win)
main()
    
