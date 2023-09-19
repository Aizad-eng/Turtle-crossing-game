import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()

screen.listen()


screen.onkey(player.up,"Up")
screen.onkey(player.down, "Down")
game_is_on = True
while game_is_on:

    time.sleep(cars.speed)
    screen.update()
    cars.create_cars()
    cars.move()

    if player.ycor()>=280:
        scoreboard.increment_score()
        cars.increase_speed()
        player.return_to_origin()
    for car in cars.all_cars:
        if car.distance(player)<=15:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()