import time
from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep



screen = Screen()
screen.bgcolor ("black")
screen.setup (width = 800 , height = 600)
screen.title("SIM'S PONG GAME ")
screen.tracer(0)

#object creation for 2 paddles ryt  & left
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on :
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision b/w wall and ball
    if ball.ycor ()>280 or ball.ycor ()<-280 :
        # it needs to bounce
        ball.bounce_y()


        # Detect collision b/w ball & paddle
        #ball is of 20px and paddle is also of 20px ,thus, we're checking for distance to be less than 50
        #>340 is showcasing if it is on ryt side or left side
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect ryt side paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect ryt side paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()