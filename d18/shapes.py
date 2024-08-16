from turtle import *
import random

jen = Turtle()
screen = Screen()

colors = ["deep pink" , "indigo","khaki" ,"medium aquamarine","medium blue" , "light steel blue" , "green yellow"]
def draw_shapes( num_of_sides ) :
    for i in range ( num_of_sides):
        angle = 360 / num_of_sides
        jen.left(angle)
        jen.forward(100)

for shape_side in range (3,11) :
    jen.color(random.choice(colors))
    draw_shapes(shape_side)         #we are calling the draw_shapes function for sides ranging from 3 to 10

screen.exitonclick()