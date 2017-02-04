Last login: Mon Mar 30 18:25:34 on ttys004
MBPro ~> ipython
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
Type "copyright", "credits" or "license" for more information.

IPython 2.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import turtle

In [2]: turtle.Sc
turtle.Screen          turtle.ScrolledCanvas  

In [2]: turtle.Screen
turtle.Screen

In [2]: turtle.
Display all 175 possibilities? (y or n)
turtle.Canvas               turtle.isnan
turtle.Pen                  turtle.isvisible
turtle.RawPen               turtle.join
turtle.RawTurtle            turtle.ldexp
turtle.Screen               turtle.left
turtle.ScrolledCanvas       turtle.lgamma
turtle.Shape                turtle.listen
turtle.TK                   turtle.log
turtle.TNavigator           turtle.log10
turtle.TPen                 turtle.log1p
turtle.Tbuffer              turtle.lt
turtle.Terminator           turtle.mainloop
turtle.Turtle               turtle.math
turtle.TurtleGraphicsError  turtle.methodname
turtle.TurtleScreen         turtle.mode
turtle.TurtleScreenBase     turtle.modf
turtle.Vec2D                turtle.onclick
turtle.acos                 turtle.ondrag
turtle.acosh                turtle.onkey
turtle.addshape             turtle.onrelease
turtle.asin                 turtle.onscreenclick
turtle.asinh                turtle.ontimer
turtle.atan                 turtle.os
turtle.atan2                turtle.pd
turtle.atanh                turtle.pen
turtle.back                 turtle.pencolor
turtle.backward             turtle.pendown
turtle.begin_fill           turtle.pensize
turtle.begin_poly           turtle.penup
turtle.bgcolor              turtle.pi
turtle.bgpic                turtle.pos
turtle.bk                   turtle.position
turtle.bye                  turtle.pow
turtle.ceil                 turtle.pu
turtle.circle               turtle.radians
turtle.clear                turtle.read_docstrings
turtle.clearscreen          turtle.readconfig
turtle.clearstamp           turtle.register_shape
turtle.clearstamps          turtle.reset
turtle.clone                turtle.resetscreen
turtle.color                turtle.resizemode
turtle.colormode            turtle.right
turtle.config_dict          turtle.rt
turtle.copysign             turtle.screensize
turtle.cos                  turtle.seth
turtle.cosh                 turtle.setheading
turtle.deepcopy             turtle.setpos
turtle.degrees              turtle.setposition
turtle.delay                turtle.settiltangle
turtle.distance             turtle.setundobuffer
turtle.done                 turtle.setup
turtle.dot                  turtle.setworldcoordinates
turtle.down                 turtle.setx
turtle.e                    turtle.sety
turtle.end_fill             turtle.shape
turtle.end_poly             turtle.shapesize
turtle.erf                  turtle.showturtle
turtle.erfc                 turtle.sin
turtle.exitonclick          turtle.sinh
turtle.exp                  turtle.speed
turtle.expm1                turtle.split
turtle.fabs                 turtle.sqrt
turtle.factorial            turtle.st
turtle.fd                   turtle.stamp
turtle.fill                 turtle.tan
turtle.fillcolor            turtle.tanh
turtle.floor                turtle.tilt
turtle.fmod                 turtle.tiltangle
turtle.forward              turtle.time
turtle.frexp                turtle.title
turtle.fsum                 turtle.towards
turtle.gamma                turtle.tracer
turtle.get_poly             turtle.trunc
turtle.getcanvas            turtle.turtles
turtle.getmethparlist       turtle.turtlesize
turtle.getpen               turtle.types
turtle.getscreen            turtle.undo
turtle.getshapes            turtle.undobufferentries
turtle.getturtle            turtle.up
turtle.goto                 turtle.update
turtle.heading              turtle.width
turtle.hideturtle           turtle.window_height
turtle.home                 turtle.window_width
turtle.ht                   turtle.write
turtle.hypot                turtle.write_docstringdict
turtle.isdown               turtle.xcor
turtle.isfile               turtle.ycor
turtle.isinf                

In [2]: turtle.TurtleScreen?
Type:            type
String form:     <class 'turtle.TurtleScreen'>
File:            /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.py
Init definition: turtle.TurtleScreen(self, cv, mode='standard', colormode=1.0, delay=10)
Docstring:
Provides screen oriented methods like setbg etc.

Only relies upon the methods of TurtleScreenBase and NOT
upon components of the underlying graphics toolkit -
which is Tkinter in this case.

In [3]: cohen_screen = turtle.Screen()

In [4]: co
%colors       coerce        compile       continue      
%config       cohen_screen  complex       copyright     

In [4]: cohen_screen.
cohen_screen.addshape             cohen_screen.onkey
cohen_screen.bgcolor              cohen_screen.onscreenclick
cohen_screen.bgpic                cohen_screen.ontimer
cohen_screen.bye                  cohen_screen.register_shape
cohen_screen.canvheight           cohen_screen.reset
cohen_screen.canvwidth            cohen_screen.resetscreen
cohen_screen.clear                cohen_screen.screensize
cohen_screen.clearscreen          cohen_screen.setup
cohen_screen.colormode            cohen_screen.setworldcoordinates
cohen_screen.cv                   cohen_screen.title
cohen_screen.delay                cohen_screen.tracer
cohen_screen.exitonclick          cohen_screen.turtles
cohen_screen.getcanvas            cohen_screen.update
cohen_screen.getshapes            cohen_screen.window_height
cohen_screen.listen               cohen_screen.window_width
cohen_screen.mode                 cohen_screen.xscale
cohen_screen.onclick              cohen_screen.yscale

In [4]: cohen_screen.xscale
Out[4]: 1.0

In [5]: cohen_screen.turtles
Out[5]: <bound method _Screen.turtles of <turtle._Screen object at 0x1023d81d0>>

In [6]: cohen_screen.turtles()
Out[6]: []

In [7]: turtle.T
turtle.TK                   turtle.Turtle
turtle.TNavigator           turtle.TurtleGraphicsError
turtle.TPen                 turtle.TurtleScreen
turtle.Tbuffer              turtle.TurtleScreenBase
turtle.Terminator           

In [7]: turtle.Tur
turtle.Turtle               turtle.TurtleScreen
turtle.TurtleGraphicsError  turtle.TurtleScreenBase

In [7]: cohen = turtle.Turtle()

In [8]: cohen.left?
Type:        instancemethod
String form: <bound method Turtle.left of <turtle.Turtle object at 0x102166d50>>
File:        /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.py
Definition:  cohen.left(self, angle)
Docstring:
Turn turtle left by angle units.

Aliases: left | lt

Argument:
angle -- a number (integer or float)

Turn turtle left by angle units. (Units are by default degrees,
but can be set via the degrees() and radians() functions.)
Angle orientation depends on mode. (See this.)

Example (for a Turtle instance named turtle):
>>> turtle.heading()
22.0
>>> turtle.left(45)
>>> turtle.heading()
67.0

In [9]: turtle.left(1000000000)
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-9-dbbb98990d31> in <module>()
----> 1 turtle.left(1000000000)

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in left(angle)

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in left(self, angle)
   1612         67.0
   1613         """
-> 1614         self._rotate(angle)
   1615 
   1616     def pos(self):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _rotate(self, angle)
   3106             for _ in range(steps):
   3107                 self._orient = self._orient.rotate(delta)
-> 3108                 self._update()
   3109         self._orient = neworient
   3110         self._update()

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _update(self)
   2564             self._update_data()
   2565             self._drawturtle()
-> 2566             screen._update()                  # TurtleScreenBase
   2567             screen._delay(screen._delayvalue) # TurtleScreenBase
   2568         else:

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _update(self)
    584         """Redraw graphics items on canvas
    585         """
--> 586         self.cv.update()
    587 
    588     def _delay(self, delay):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/Tkinter.pyc in update(self)
    960     def update(self):
    961         """Enter event loop until all pending events have been processed by Tcl."""
--> 962         self.tk.call('update')
    963     def update_idletasks(self):
    964         """Enter event loop until all idle callbacks have been called. This

KeyboardInterrupt: 

In [10]: 

In [10]: turtle.forward(100)

In [11]: co
%colors       coerce        cohen_screen  complex       copyright
%config       cohen         compile       continue      

In [11]: cohen.
cohen.DEFAULT_ANGLEOFFSET  cohen.pen
cohen.DEFAULT_ANGLEORIENT  cohen.pencolor
cohen.DEFAULT_MODE         cohen.pendown
cohen.START_ORIENTATION    cohen.pensize
cohen.back                 cohen.penup
cohen.backward             cohen.pos
cohen.begin_fill           cohen.position
cohen.begin_poly           cohen.pu
cohen.bk                   cohen.radians
cohen.circle               cohen.reset
cohen.clear                cohen.resizemode
cohen.clearstamp           cohen.right
cohen.clearstamps          cohen.rt
cohen.clone                cohen.screen
cohen.color                cohen.screens
cohen.currentLine          cohen.seth
cohen.currentLineItem      cohen.setheading
cohen.degrees              cohen.setpos
cohen.distance             cohen.setposition
cohen.dot                  cohen.settiltangle
cohen.down                 cohen.setundobuffer
cohen.drawingLineItem      cohen.setx
cohen.end_fill             cohen.sety
cohen.end_poly             cohen.shape
cohen.fd                   cohen.shapesize
cohen.fill                 cohen.showturtle
cohen.fillcolor            cohen.speed
cohen.forward              cohen.st
cohen.get_poly             cohen.stamp
cohen.getpen               cohen.stampItems
cohen.getscreen            cohen.tilt
cohen.getturtle            cohen.tiltangle
cohen.goto                 cohen.towards
cohen.heading              cohen.tracer
cohen.hideturtle           cohen.turtle
cohen.home                 cohen.turtlesize
cohen.ht                   cohen.undo
cohen.isdown               cohen.undobuffer
cohen.isvisible            cohen.undobufferentries
cohen.items                cohen.up
cohen.left                 cohen.width
cohen.lt                   cohen.window_height
cohen.onclick              cohen.window_width
cohen.ondrag               cohen.write
cohen.onrelease            cohen.xcor
cohen.pd                   cohen.ycor

In [11]: cohen.ba
cohen.back      cohen.backward  

In [11]: cohen.right(45)

In [12]: cohen.forward(100)

In [13]: cohen.undo
Out[13]: <bound method Turtle.undo of <turtle.Turtle object at 0x102166d50>>

In [14]: cohen.undo()

In [15]: cohen.undo()

In [16]: turtle.und
turtle.undo               turtle.undobufferentries  

In [16]: turtle.undo()

In [17]: del(turtle)

In [18]: turtle.forward(100)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-18-3181c32e0c8c> in <module>()
----> 1 turtle.forward(100)

NameError: name 'turtle' is not defined

In [19]: cohen.forward(100)

In [20]: cohen.right(45)

In [21]: cohen.right(45)

In [22]: cohen.forward(100)

In [23]: coh
cohen         cohen_screen  

In [23]: cohen.right(90)

In [24]: cohen.forward(100)

In [25]: cohen.right(90)

In [26]: cohen.forward(100)

In [27]: def square(length):
   ....:     cohen.forward(100)
   ....:     cohen.right(90)
   ....:     cohen.forward(100)
   ....:     cohen.right(90)
   ....:     cohen.forward(100)
   ....:     cohen.right(90)
   ....:     cohen.forward(100)
   ....:     

In [28]: square(1000000)

In [29]: def square(length):
    cohen.forward(length)
    cohen.right(90)
    cohen.forward(length)
    cohen.right(90)
    cohen.forward(length)
    cohen.right(90)
    cohen.forward(length)
   ....:     

In [30]: cohen.speed(10)

In [31]: square(1000000)
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-31-aca4f2ab16e9> in <module>()
----> 1 square(1000000)

<ipython-input-29-67d2438b8e42> in square(length)
      1 def square(length):
----> 2     cohen.forward(length)
      3     cohen.right(90)
      4     cohen.forward(length)
      5     cohen.right(90)

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in forward(self, distance)
   1550         (-50.00,0.00)
   1551         """
-> 1552         self._go(distance)
   1553 
   1554     def back(self, distance):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _go(self, distance)
   1518         """move turtle forward by specified distance"""
   1519         ende = self._position + self._orient * distance
-> 1520         self._goto(ende)
   1521 
   1522     def _rotate(self, angle):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _goto(self, end)
   3009                                      (start, self._position),
   3010                                      self._pencolor, self._pensize, top)
-> 3011                 self._update()
   3012             if self._drawing:
   3013                 screen._drawline(self.drawingLineItem, ((0, 0), (0, 0)),

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _update(self)
   2564             self._update_data()
   2565             self._drawturtle()
-> 2566             screen._update()                  # TurtleScreenBase
   2567             screen._delay(screen._delayvalue) # TurtleScreenBase
   2568         else:

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _update(self)
    584         """Redraw graphics items on canvas
    585         """
--> 586         self.cv.update()
    587 
    588     def _delay(self, delay):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/Tkinter.pyc in update(self)
    960     def update(self):
    961         """Enter event loop until all pending events have been processed by Tcl."""
--> 962         self.tk.call('update')
    963     def update_idletasks(self):
    964         """Enter event loop until all idle callbacks have been called. This

KeyboardInterrupt: 

In [32]: square(1000000)
Display all 377 possibilities? (y or n)
%%!                        _
%%HTML                     _13
%%SVG                      _4
%%bash                     _5
%%capture                  _6
%%debug                    __
%%file                     __IPYTHON__
%%html                     __IPYTHON__active
%%javascript               ___
%%latex                    __builtin__
%%perl                     __debug__
%%prun                     __doc__
%%pypy                     __import__
%%python                   __name__
%%python2                  __package__
%%python3                  _dh
%%ruby                     _i
%%script                   _i1
%%sh                       _i10
%%svg                      _i11
%%sx                       _i12
%%system                   _i13
%%time                     _i14
%%timeit                   _i15
%%writefile                _i16
%alias                     _i17
%alias_magic               _i18
%autocall                  _i19
%autoindent                _i2
%automagic                 _i20
%bookmark                  _i21
%cat                       _i22
%cd                        _i23
%clear                     _i24
%colors                    _i25
%config                    _i26
%cp                        _i27
%cpaste                    _i28
%debug                     _i29
%dhist                     _i3
%dirs                      _i30
%doctest_mode              _i31
%ed                        _i4
%edit                      _i5
%env                       _i6
%gui                       _i7
%hist                      _i8
%history                   _i9
%install_default_config    _ih
%install_ext               _ii
%install_profiles          _iii
%killbgscripts             _oh
%ldir                      _sh
%less                      abs
%lf                        all
%lk                        and
%ll                        any
%load                      apply
%load_ext                  artifacts
%loadpy                    as
%logoff                    assert
%logon                     basestring
%logstart                  bin
%logstate                  bool
%logstop                   break
%ls                        buffer
%lsmagic                   bytearray
%lx                        bytes
%macro                     callable
%magic                     chr
%man                       class
%matplotlib                classmethod
%mkdir                     cmp
%more                      coerce
%mv                        cohen
%notebook                  cohen_screen
%page                      compile
%paste                     complex
%pastebin                  continue
%pdb                       copyright
%pdef                      credits
%pdoc                      def
%pfile                     del
%pinfo                     delattr
%pinfo2                    dict
%popd                      dir
%pprint                    divmod
%precision                 dreload
%profile                   elif
%prun                      else
%psearch                   enumerate
%psource                   eval
%pushd                     except
%pwd                       exec
%pycat                     execfile
%pylab                     exit
%quickref                  file
%recall                    filter
%rehashx                   finally
%reload_ext                float
%rep                       for
%rerun                     format
%reset                     from
%reset_selective           frozenset
%rm                        get_ipython
%rmdir                     getattr
%run                       global
%save                      globals
%sc                        hasattr
%store                     hash
%sx                        help
%system                    hex
%tb                        id
%time                      if
%timeit                    import
%unalias                   in
%unload_ext                input
%who                       int
%who_ls                    intern
%whos                      is
%xdel                      isinstance
%xmode                     issubclass
4lA0z0k.jpg                iter
Applications               kids_sessions
ArithmeticError            lambda
AssertionError             len
AttributeError             license
BACKUP_2014                list
BACKUP_2014.tar            locals
BaseException              lock.patch
BufferError                long
BytesWarning               map
DeprecationWarning         max
Desktop                    memoryview
Documents                  min
Downloads                  next
EOFError                   not
Ellipsis                   object
EnvironmentError           oct
Exception                  onoff.py
False                      open
FloatingPointError         or
FutureWarning              ord
GeneratorExit              pass
IOError                    patches
ImportError                plans
ImportWarning              play
In                         pow
IndentationError           print
IndexError                 property
KeyError                   quit
KeyboardInterrupt          raise
Library                    range
LookupError                raw_input
MemoryError                recordings
Movies                     reduce
Music                      reload
NameError                  repr
None                       return
NotImplemented             reversed
NotImplementedError        round
OSError                    set
Out                        setattr
OverflowError              slice
PendingDeprecationWarning  sorted
Pictures                   square
Public                     ssh_config
ReferenceError             staticmethod
RuntimeError               str
RuntimeWarning             sum
StandardError              super
StopIteration              tc.py
SyntaxError                teo_university
SyntaxWarning              try
SystemError                tuple
SystemExit                 type
TabError                   unichr
True                       unicode
TypeError                  vars
UnboundLocalError          virt_envs
UnicodeDecodeError         vmlocker.py
UnicodeEncodeError         while
UnicodeError               with
UnicodeTranslateError      work
UnicodeWarning             writing
UserWarning                xrange
ValueError                 yield
Warning                    zip
ZeroDivisionError          

In [32]: 

In [32]: cohen.speed(0)

In [33]: square(1000000)

In [34]: cohen.goto(0)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-a2bc244430b0> in <module>()
----> 1 cohen.goto(0)

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in goto(self, x, y)
   1687         """
   1688         if y is None:
-> 1689             self._goto(Vec2D(*x))
   1690         else:
   1691             self._goto(Vec2D(x, y))

TypeError: type object argument after * must be a sequence, not int

In [35]: cohen.goto(0,0)

In [36]: square(1000000)

In [37]: square(1000000)

In [38]: square(1000000)

In [39]: square(1000000)

In [40]: cohen_screen.cle
cohen_screen.clear        cohen_screen.clearscreen  

In [40]: cohen_screen.
cohen_screen.addshape             cohen_screen.onkey
cohen_screen.bgcolor              cohen_screen.onscreenclick
cohen_screen.bgpic                cohen_screen.ontimer
cohen_screen.bye                  cohen_screen.register_shape
cohen_screen.canvheight           cohen_screen.reset
cohen_screen.canvwidth            cohen_screen.resetscreen
cohen_screen.clear                cohen_screen.screensize
cohen_screen.clearscreen          cohen_screen.setup
cohen_screen.colormode            cohen_screen.setworldcoordinates
cohen_screen.cv                   cohen_screen.title
cohen_screen.delay                cohen_screen.tracer
cohen_screen.exitonclick          cohen_screen.turtles
cohen_screen.getcanvas            cohen_screen.update
cohen_screen.getshapes            cohen_screen.window_height
cohen_screen.listen               cohen_screen.window_width
cohen_screen.mode                 cohen_screen.xscale
cohen_screen.onclick              cohen_screen.yscale

In [40]: cohen_screen.cl
cohen_screen.clear        cohen_screen.clearscreen  

In [40]: cohen_screen.clear
cohen_screen.clear        cohen_screen.clearscreen  

In [40]: cohen_screen.clearscreen
Out[40]: <bound method _Screen.clear of <turtle._Screen object at 0x1023d81d0>>

In [41]: cohen_screen.clearscreen()

In [42]: cohen.goto(0,0)

In [43]: import turtle

In [44]: cohen = turtle.Tur
turtle.Turtle               turtle.TurtleScreen
turtle.TurtleGraphicsError  turtle.TurtleScreenBase

In [44]: cohen = turtle.Turtle()

In [45]: for i in range(100):
   ....:     print i
   ....:     
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99

In [46]: for i in range(100):
    square(i)
   ....:     

In [47]: cohen.speed(0)

In [48]: range(100)
Out[48]: 
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33,
 34,
 35,
 36,
 37,
 38,
 39,
 40,
 41,
 42,
 43,
 44,
 45,
 46,
 47,
 48,
 49,
 50,
 51,
 52,
 53,
 54,
 55,
 56,
 57,
 58,
 59,
 60,
 61,
 62,
 63,
 64,
 65,
 66,
 67,
 68,
 69,
 70,
 71,
 72,
 73,
 74,
 75,
 76,
 77,
 78,
 79,
 80,
 81,
 82,
 83,
 84,
 85,
 86,
 87,
 88,
 89,
 90,
 91,
 92,
 93,
 94,
 95,
 96,
 97,
 98,
 99]

In [49]: range(100, 200)
Out[49]: 
[100,
 101,
 102,
 103,
 104,
 105,
 106,
 107,
 108,
 109,
 110,
 111,
 112,
 113,
 114,
 115,
 116,
 117,
 118,
 119,
 120,
 121,
 122,
 123,
 124,
 125,
 126,
 127,
 128,
 129,
 130,
 131,
 132,
 133,
 134,
 135,
 136,
 137,
 138,
 139,
 140,
 141,
 142,
 143,
 144,
 145,
 146,
 147,
 148,
 149,
 150,
 151,
 152,
 153,
 154,
 155,
 156,
 157,
 158,
 159,
 160,
 161,
 162,
 163,
 164,
 165,
 166,
 167,
 168,
 169,
 170,
 171,
 172,
 173,
 174,
 175,
 176,
 177,
 178,
 179,
 180,
 181,
 182,
 183,
 184,
 185,
 186,
 187,
 188,
 189,
 190,
 191,
 192,
 193,
 194,
 195,
 196,
 197,
 198,
 199]

In [50]: for i in range(100, 1000):
   ....:     square(i)
   ....:     
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-50-163f6673a29a> in <module>()
      1 for i in range(100, 1000):
----> 2     square(i)
      3 

<ipython-input-29-67d2438b8e42> in square(length)
      3     cohen.right(90)
      4     cohen.forward(length)
----> 5     cohen.right(90)
      6     cohen.forward(length)
      7     cohen.right(90)

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in right(self, angle)
   1591         337.0
   1592         """
-> 1593         self._rotate(-angle)
   1594 
   1595     def left(self, angle):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _rotate(self, angle)
   3108                 self._update()
   3109         self._orient = neworient
-> 3110         self._update()
   3111 
   3112     def _newLine(self, usePos=True):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _update(self)
   2564             self._update_data()
   2565             self._drawturtle()
-> 2566             screen._update()                  # TurtleScreenBase
   2567             screen._delay(screen._delayvalue) # TurtleScreenBase
   2568         else:

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/turtle.pyc in _update(self)
    584         """Redraw graphics items on canvas
    585         """
--> 586         self.cv.update()
    587 
    588     def _delay(self, delay):

/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/Tkinter.pyc in update(self)
    960     def update(self):
    961         """Enter event loop until all pending events have been processed by Tcl."""
--> 962         self.tk.call('update')
    963     def update_idletasks(self):
    964         """Enter event loop until all idle callbacks have been called. This

KeyboardInterrupt: 

In [51]: coh
cohen         cohen_screen  

In [51]: cohen_screen.getcanvas()
Out[51]: <turtle.ScrolledCanvas instance at 0x102167ef0>

In [52]: _51.postscript(file='cohen.eps')
Out[52]: ''

In [53]: 
Do you really want to exit ([y]/n)? 
MBPro ~> 

