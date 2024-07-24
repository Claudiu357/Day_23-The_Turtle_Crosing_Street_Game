import random
import time
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CHANCE = [0, 0, 0, 0, 0, 1]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.last_y = None
        self.hideturtle()
        self.all_cars = []
        self.Y_POS = []
        for _ in range(-220, 231, 20):
            self.Y_POS.append(_)

    def add_car(self):
        t = Turtle()
        t.shape("square")
        t.penup()
        t.shapesize(stretch_len=2, stretch_wid=1)
        t.color(random.choice(COLORS))
        t.setheading(180)
        random_y = random.choice(self.Y_POS)
        t.goto(x=300, y=random_y)
        self.all_cars.append(t)

    def move_cars(self):
        if random.choice(CHANCE) == 1:
            self.add_car()
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
