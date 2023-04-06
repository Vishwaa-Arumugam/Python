from turtle import Turtle

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-280, 280)
        self.pendown()
        # self.fillcolor("red")
        self.pensize(5)
        self.goto(280, 280)
        self.goto(280, -280)
        self.goto(-280, -280)
        self.goto(-280, 280)
        