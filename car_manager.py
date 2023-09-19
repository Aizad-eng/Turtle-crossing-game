
from turtle import  Turtle
import random

COLORS = ["red", "orange", "violet", "indigo","pink", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = 0.1

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=3)
            new_car.setheading(180)
            new_y = random.randint(-210, 210)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed *=0.9

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
