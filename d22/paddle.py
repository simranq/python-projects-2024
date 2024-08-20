from turtle import  Turtle
#Create and move a paddle
#remember that all turtles begin with 20X20
class Paddle (Turtle):

    def __init__(self , position):
        super().__init__()
        #paddle = Turtle()  super keyword inherits all the Turtle() class k fxns
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5 , stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up (self):
        new_y = self.ycor() + 30
        self.goto(self.xcor() , new_y)

    def go_down (self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)


