# turtleart

## install

      pip install turtleart

## run

Main way to use turtleart right away is with the qturtle CLI command. Once
installed, just run:

      qturtle

## have fun

Running qturtle creates a screen and graph lines and your own turtle, named
whatever you'd like. At this point you can use methods defined in the
[Turtle Class](https://docs.python.org/2/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions)
and in turtleart.draw module.

## example with standard commands

* Note that we actually name the turtle variable based on user input. Some inputs won't work, but it's cute.

$ qturtle 
What is the turtle's name?> myturt
DEBUG:root:Creating turtle named: myturt
DEBUG:root:Making a screen
DEBUG:root:Setting myturt's speed to 10 to go FAST.
DEBUG:root:Making a graph to give some orientation.
Python 2.7.12 (default, Jun 29 2016, 14:05:02) 
Type "copyright", "credits" or "license" for more information.

IPython 5.2.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: myturt?
Type:        Turtle
String form: <turtle.Turtle object at 0x111c15890>
File:        /usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.py
Docstring:  
RawTurtle auto-creating (scrolled) canvas.

When a Turtle object is created or a function derived from some
Turtle method is called a TurtleScreen object is automatically created.

In [2]: myturt.color()
Out[2]: ('black', 'black')

In [3]: myturt.right(50)

In [4]: myturt.forward(50)

In [5]: myturt.right(50)

In [6]: myturt.forward(50)

## example with turtle commands (continued in ipython shell)

* In this example we pass our Turtle object into helper methods to draw things.

In [7]: import turtleart.draw

In [8]: turtleart.draw.drawline?
Signature: turtleart.draw.drawline(turt, a, b, c, d)
Docstring: <no docstring>
File:      ~/play/venvs/yo5/lib/python2.7/site-packages/turtleart/draw.py
Type:      function

In [9]: turtleart.draw.drawline(myturt, 100, 100, -100, -100)

In [10]: turtleart.draw.draw_quad?
Signature: turtleart.draw.draw_quad(turt, quad_num, size, count=10)
Docstring: <no docstring>
File:      ~/play/venvs/yo5/lib/python2.7/site-packages/turtleart/draw.py
Type:      function

In [11]: turtleart.draw.draw_quad(myturt, 1, 15, 30)
