import turtle
from turtle import *
t = Turtle()
t.shape('turtle')



def rectangle():
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle()

def triangle(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
triangle(90)    
    