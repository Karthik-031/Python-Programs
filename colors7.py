Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> colors=["red","purple","blue","green","orange","yellow"]
>>> my_pen=turtle.pen()
>>> turtle.bgcolor("black")
>>> for x in range(360):
	my_pen.pencolor(color[x%6])
	my_pen.width(x/100+1)
	my_pen.forward(x)
	my_pen.left(59)
	.
	
SyntaxError: invalid syntax
>>> import turtle
>>> t=turtle.turtle()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t=turtle.turtle()
AttributeError: module 'turtle' has no attribute 'turtle'
>>> import turtle
>>> t=turtle.Turtle()
>>> t.forward(100)
>>> turtle.mainloop()
