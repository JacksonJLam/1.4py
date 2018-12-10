# futvalgraph.py
# by Jackson Lambert
# updated the future value program to be graphical

from graphics import *

def main():
    # Introduction
    print ("This program plots the growth of a 10-year investment.")
    win = GraphWin("Investment Growth Chart", 320, 240)
    inputs = GraphWin("Input Your Data")
    win.setBackground("white")
    # Get principal and interest rate
    Text(Point(75,75),"Set Your Principal").draw(inputs)
    Text(Point(75,125),"Set Your APR").draw(inputs)
    input2 = Entry(Point(100,150), 20)
    input1 = Entry(Point(100,100), 20)
    input1.draw(inputs)
    input2.draw(inputs)
    calc = Text(Point(100,175), "Click Here To Calculate")
    calc.draw(inputs)
    inputs.getMouse()
    principal = float(input1.getText())
    apr= float(input2.getText())
   
    # Create a graphics window with labels on left edge
    
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle (Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range (1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height ))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    Text(Point(100,10), "Click Twice Anywhere to Exit")
    win.getMouse()
    win.getMouse()
    win.close()
    inputs.close()

main()
