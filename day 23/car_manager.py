from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_car = []
    
    def create_car(self):
        creatiion_car = random.randint(1, 6)
        if creatiion_car == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            car.goto(300, y)
            self.all_car.append(car)
    
    def move_car(self):
        for self.car in self.all_car:
            self.car.backward(STARTING_MOVE_DISTANCE)
    
    def increse_speed(self):
        for car in self.all_car:
            car.speed(6+MOVE_INCREMENT)
        