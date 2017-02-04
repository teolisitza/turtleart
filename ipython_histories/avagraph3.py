Last login: Mon Mar 30 19:49:46 on ttys000
MBPro ~> cd kids_sessions/
MBPro kids_sessions> ls
ava.eps         ava_3_3_15.out      ava_graph2.out
ava2.eps        ava_advanced.png    avagraph.out
ava3.eps        ava_graph.eps       avagraph2.out
ava4.eps        ava_graph.png       cohen_crazy_square.out
MBPro kids_sessions> mkdir packages
MBPro kids_sessions> cd packages/
MBPro packages> vim avaturtle.py
MBPro packages> cd ..
MBPro kids_sessions> ls
ava.eps         ava_advanced.png    avagraph2.out
ava2.eps        ava_graph.eps       cohen_crazy_square.out
ava3.eps        ava_graph.png       packages
ava4.eps        ava_graph2.out
ava_3_3_15.out      avagraph.out
MBPro kids_sessions> PYTHONPATH=`pwd`/packages ipython
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
Type "copyright", "credits" or "license" for more information.

IPython 2.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import avaturtle

In [2]: avaturtle.drawline?
Type:        function
String form: <function drawline at 0x10d860578>
File:        /Users/teo/kids_sessions/packages/avaturtle.py
Definition:  avaturtle.drawline(turt, a, b, c, d)
Docstring:   <no docstring>

In [3]: import turtle

In [4]: ava = turtle.Turtle()

In [5]: avaturtle.drawline(ava, 0,0, 30,30)

In [6]: ava.un
ava.undo               ava.undobuffer         ava.undobufferentries

In [6]: ava.undo()

In [7]: def makegraph(turt):
   ...:     turt.drawline(-1000, 0, 1000, 0)
   ...:     turt.drawline
   ...:     

In [8]: def makegraph(turt):

KeyboardInterrupt

In [8]: def makegraph(turt):
   ...:     avaturtle.drawline(turt, -1000, 0, 1000, 0)
   ...:     avaturtle.drawline(turt, 0, -1000, 0, 1000)
   ...:     

In [9]: ava.speed(10)

In [10]: makegraph(ava)

In [11]: edit packages/
packages/avaturtle.py   packages/avaturtle.pyc  

In [11]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [12]: 
Do you really want to exit ([y]/n)? 
MBPro kids_sessions> PYTHONPATH=`pwd`/packages ipython
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
Type "copyright", "credits" or "license" for more information.

IPython 2.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import turtle

In [2]: ava = turtle.Turtle()

In [3]: from avaturtle import *

In [4]: makegraph()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-7486f9b0e4a1> in <module>()
----> 1 makegraph()

TypeError: makegraph() takes exactly 1 argument (0 given)

In [5]: makegraph(ava)

In [6]: ava.goto(0,0)

In [7]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [8]: reload(ava
ava               ava3.eps          ava_advanced.png  ava_graph2.out
ava.eps           ava4.eps          ava_graph.eps     avagraph.out
ava2.eps          ava_3_3_15.out    ava_graph.png     avagraph2.out

In [8]: 
Do you really want to exit ([y]/n)? 
MBPro kids_sessions> PYTHONPATH=`pwd`/packages ipython
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
Type "copyright", "credits" or "license" for more information.

IPython 2.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import turtle

In [2]: ava = turtle.Turtle()

In [3]: ava.speed(10)

In [4]: import avaturtle

In [5]: avaturtle.makegraph()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-5ec8fa0eaee0> in <module>()
----> 1 avaturtle.makegraph()

TypeError: makegraph() takes exactly 1 argument (0 given)

In [6]: avaturtle.makegraph(ava)

In [7]: avaturtle.dr
avaturtle.draw_quad  avaturtle.drawline   

In [7]: avaturtle.draw_quad(ava)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-e52f6c9a2855> in <module>()
----> 1 avaturtle.draw_quad(ava)

/Users/teo/kids_sessions/packages/avaturtle.py in draw_quad(turt)
     13     y = -200
     14     while x <= 200:
---> 15         drawline(x, 0,0,y)
     16         x += 20
     17         y += 20

TypeError: drawline() takes exactly 5 arguments (4 given)

In [8]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [9]: reload(avaturtle)
Out[9]: <module 'avaturtle' from '/Users/teo/kids_sessions/packages/avaturtle.py'>

In [10]: avaturtle.draw_quad(ava)

In [11]: avaturtle.draw_quad(ava)

In [12]: avaturtle.draw_quad(ava)

In [13]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [14]: reload(avaturtle)
Out[14]: <module 'avaturtle' from '/Users/teo/kids_sessions/packages/avaturtle.py'>

In [15]: avaturtle.draw_quad(ava)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-e52f6c9a2855> in <module>()
----> 1 avaturtle.draw_quad(ava)

TypeError: draw_quad() takes exactly 2 arguments (1 given)

In [16]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [17]: avaturtle.draw_quad(ava,20)

In [18]: avaturtle.draw_quad?
Type:        function
String form: <function draw_quad at 0x1072685f0>
File:        /Users/teo/kids_sessions/packages/avaturtle.py
Definition:  avaturtle.draw_quad(turt, size)
Docstring:   <no docstring>

In [19]: avaturtle.draw_quad??
Type:        function
String form: <function draw_quad at 0x1072685f0>
File:        /Users/teo/kids_sessions/packages/avaturtle.py
Definition:  avaturtle.draw_quad(turt, size)
Source:
def draw_quad(turt, size):
    x = size
    y = -(size*10)
    while x <= 200:
        drawline(turt, x, 0,0,y)
        x += 20
        y += 20

In [20]: avaturtle.draw_quad(ava,30)

In [21]: avaturtle.draw_quad(ava,20)

In [22]: avaturtle.draw_quad(ava,10)

In [23]: avaturtle.draw_quad(ava,5)

In [24]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [25]: ava.undo
ava.undo               ava.undobuffer         ava.undobufferentries

In [25]: ava.undo()

In [26]: ava.undo()

In [27]: ava.undo()

In [28]: ava.undo()

In [29]: ava.undo()

In [30]: ava.undo()

In [31]: while True:
   ....:     ava.und()
   ....:     ava.undo()

KeyboardInterrupt

In [31]: while True:
    ava.undo()
   ....:     
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-31-5b11be272e76> in <module>()
      1 while True:
----> 2     ava.undo()
      3 

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in undo(self)
   3529         if self.undobuffer is None:
   3530             return
-> 3531         item = self.undobuffer.pop()
   3532         action = item[0]
   3533         data = item[1:]

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in pop(self)
    898                 return None
    899             else:
--> 900                 self.buffer[self.ptr] = [None]
    901                 self.ptr = (self.ptr - 1) % self.bufsize
    902                 return (item)

KeyboardInterrupt: 

In [32]: edit packages/avaturtle.py
Editing... done. Executing edited code...

In [33]: avaturtle.draw_quad(ava,50)

In [34]: avaturtle.draw_quad(ava,20)

In [35]: avaturtle.makegraph(ava)
