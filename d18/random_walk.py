import turtle as t
import random

jen = t.Turtle()
t.colormode(255)
jen.shape("arrow")


directions = [0,90,180,270]
jen.pensize(15)
jen.speed(("fastest"))

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color = ( r ,g , b )
    return random_color


for i in range (200):
    jen.color(random_color())
    jen.forward(30)
    jen.setheading(random.choice(directions))

random_color()
