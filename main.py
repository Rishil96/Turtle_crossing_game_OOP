import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_color = 'maroon'

player = Player(player_color)
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Turtle reaches finish line
    if player.new_level():
        score.update_level()
        car_manager.increase_speed()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
