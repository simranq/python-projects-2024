from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# keep in mind that earlier r cars were 20 X 20 but now their size is 20 X 40

# create and move cars
# using random_y as we have rule no 2

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()


    def create_car(self):
        random_chance = random.randint(1,6) #lyk a a die
        if random_chance ==1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2 , stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    #errors and resolutions:
# this gave me error as we need 2 arguments for both axes.
# ----> self.goto(STARTING_MOVE_DISTANCE)
