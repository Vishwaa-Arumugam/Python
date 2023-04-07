from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def up(self):
        NEW_Y = self.ycor() + 30
        self.goto(self.xcor(), NEW_Y)

    def down(self):
        NEW_Y = self.ycor() - 30
        self.goto(self.xcor(), NEW_Y)
