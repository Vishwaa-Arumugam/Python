# 1. Create a snake body
# 2. Move the snake
# 3. Conkrol the snake
# 4. Detect the collision
# 5. create a score board
# 6. create a collision wall
# 7. detect collision with tail
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collison with food using distance method
    if snake.head.distance(food) < 15:
        food.food_location()
        snake.extend()
        score.score_count()
    
    # detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    
    # detect collison with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
           score.reset()
           snake.reset()

screen.exitonclick()








