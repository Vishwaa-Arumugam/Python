import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_m = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=turtle.up)
screen.onkey(key="Down", fun=turtle.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_m.create_car()
    car_m.move_car()

    # detect collison with car
    for car in car_m.all_car:
        if car.distance(turtle) < 30:
            score.game_over()
            game_is_on = False
    
    if turtle.finish():
        turtle.goto_begening()
        car_m.increse_speed()
        score.update_score()
        score.point()
  

screen.exitonclick()