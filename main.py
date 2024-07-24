import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

LEVEL = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

scoreboard = Scoreboard()

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(LEVEL)
    screen.update()
    cars.move_cars()
    if player.finish_line():
        player.restart()
        scoreboard.level_up()
        LEVEL = LEVEL / 2.5
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()