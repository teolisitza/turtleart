import logging
logging.basicConfig(level='DEBUG')
log = logging.getLogger()

import turtle
import turtleart

turtle_name = raw_input('What is the turtle\'s name?> ')
log.debug('Creating turtle named: %s' % turtle_name)
myturtle = globals()[turtle_name] = turtle.Turtle()
log.debug('Making a screen')
screen=turtle.Screen()
log.debug('Setting %s\'s speed to 10 to go FAST.' % turtle_name)
myturtle.speed(10)
log.debug('Making a graph to give some orientation.')
turtleart.makegraph(myturtle)
myturtle.goto(0,0)

import IPython
IPython.start_ipython()
