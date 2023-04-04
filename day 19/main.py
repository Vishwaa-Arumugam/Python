from turtle import Turtle, Screen

aamai = Turtle()
# me = Turtle()
aamai.shape("turtle")
screen = Screen()


def move_forwards():
    aamai.forward(25)

def move_backwards():
    aamai.backward(25)

def turn_left():
    new_heading = aamai.heading() + 10
    aamai.setheading(new_heading)

def turn_right():
    aamai.right(10)

def clear_screen():
    aamai.clear()
    aamai.penup()
    aamai.home()
    aamai.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
