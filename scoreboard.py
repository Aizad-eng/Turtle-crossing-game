import car_manager

FONT = ("Courier", 24, "normal")
from turtle import Turtle
from car_manager import CarManager
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-50, 250)
        self.display_score()
    def increment_score(self):
        self.score+=1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=FONT)

    def game_over(self):
        self.write("Game Over", move=False, align='left', font = ("Courier", 24, "bold"))
