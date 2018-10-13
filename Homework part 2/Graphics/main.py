import graphics
win = graphics.GraphWin("My Circle", 100, 100)
c = graphics.Circle(graphics.Point(50,50), 10)
c.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done
print ("Hello world")
