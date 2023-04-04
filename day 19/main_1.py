from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color : ")
# print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for i in range(0, 6):
    aamai = Turtle(shape="turtle")
    aamai.color(color[i])
    aamai.penup()
    aamai.goto(x=-230, y=y)
    y += 30
    all_turtles.append(aamai)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for aamai in all_turtles:
        if aamai.xcor() > 230:
            is_race_on = False
            winner = aamai.pencolor()
            if winner == user_bet:
                print(f"You've won! the {winner} turtle is the winner")
            else:
                print(f"You've lost :( the {winner} turtle is the winner")

        random_distance = random.randint(0, 10)
        aamai.forward(random_distance)

screen.exitonclick()
