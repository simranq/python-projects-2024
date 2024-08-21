from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# RULE 1: Only up key functions
#RULE 2: Cars are randomly generated along the y-axis
#        and will move from the right edge of the screen to the left edge.
class Player(Turtle):
   def __init__(self):
       super().__init__()
       self.shape("turtle")
       self.penup()
       self.go_to_start()
       #now, since turtle would be facingeast let's turn it towards north
       self.setheading(90)

   def go_to_start(self):
       self.goto(STARTING_POSITION)
   def go_up(self):
       self.forward(MOVE_DISTANCE)

   def is_at_finish_line(self):
        if self.ycor() < FINISH_LINE_Y :
            return True

