import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# will turn off unnecessary animations,  and we can update
# it using update() whenever we wanna have those sick animations.

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
        # checks the distance between the car manager class's object + player class's object
    for car in car_manager.all_cars :
        if car.distance(player) < 20:
            game_is_on = False

# detects if the turtle reaches the other side
    if player.is_at_finish_line():
        player.go_to_start()
        # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
