import random
import turtle as t
from turtle import *

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color = ( r ,g , b )
    return color

def draw_spirograph(size_of_gap):
    for i in range (int( 360 / size_of_gap)):
        jen.color(random_color())
        jen.circle(100)
        jen.setheading(jen.heading() + size_of_gap )


jen = t.Turtle()
jen.speed("fastest")
t.colormode(255)

draw_spirograph(3)


screen = t.Screen()
screen.exitonclick()