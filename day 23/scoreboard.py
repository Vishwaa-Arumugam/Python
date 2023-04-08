from turtle import Turtle
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"LEVEL : {self.score}", align="center", font= FONT)
    
    def point(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ", align="center", font = ("Courier", 20, "normal"))
