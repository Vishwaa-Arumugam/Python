# create the screen
# create and move the paddle
# create another paddle
# create a ball
# detect collison with wall
# datect collison with paddle
# collison with paddle

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score_Board

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
score = Score_Board()

screen.listen()
screen.onkey(key="Up", fun=paddle_1.up)
screen.onkey(key="Down", fun=paddle_1.down)
screen.onkey(key="w", fun=paddle_2.up)
screen.onkey(key="s", fun=paddle_2.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # it needs to bounce
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect paddle_1
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect paddle_2
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
