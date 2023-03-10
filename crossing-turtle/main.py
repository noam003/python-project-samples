import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
cars = []

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.update_cars()

    crash_occur = car_manager.crash(player)
    if crash_occur:
        scoreboard.game_over()


    won_game = player.won_check()
    scoreboard.update_score(won_game)

screen.exitonclick()


