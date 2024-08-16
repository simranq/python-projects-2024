
from turtle import *
jen = Turtle()
screen = Screen()

#jen.shape("arrow")

'''
DIRECT A SQUARE
jen.forward(100)
jen.right(90)
jen.forward(100)
jen.right(90)
jen.forward(100)
jen.right(90)
jen.forward(100)

'''

'''

# DRAW A DASHED LINE
for i in range(15) :
    jen.color("black")
    jen.forward(10)
    jen.color("white")
    jen.forward(10)


'''
'''
#Draw a dashed line using methods

for i in range (20):
    jen.forward(10)
    jen.penup()
    jen.forward(10)
    jen.pendown()

'''
'''
#Draw a pentagon

for i in range(5):
    jen.left(72)
    jen.forward(100)

'''
'''

#Draw a hexagon

for i in range(6):
    jen.left(60)
    jen.forward(100)

'''

#Draw a hexagon


screen.exitonclick()
