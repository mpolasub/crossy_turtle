from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        random_spawn = randint(1, 6)
        if random_spawn == 1:
            car = Turtle("square")
            car.penup()
            car.color(choice(COLORS))
            car.goto(310, randint(-250, 250))
            car.shapesize(stretch_len=2, stretch_wid=1)
            self.all_cars.append(car)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
