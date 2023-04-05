from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Aerial', 12, 'normal')
ALIGN = "center"
SS = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.high_score_num = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        with open("D:\\100P\\day 20 -21\\data.txt", mode="r") as file:
            c = file.read()
        self.write(arg=f"YOUR SCORE : {self.score_num}, HIGH SCORE : {int(c)}", move=False, align=ALIGN, font=FONT)

    def score_count(self):
        self.score_num += 1
        self.clear()
        self.write(arg=f"YOUR SCORE : {self.score_num}, HIGH SCORE : {self.high_score_num}", move=False, align=ALIGN,
                   font=FONT)

    def reset(self):
        if self.score_num > self.high_score_num:
            self.high_score_num = self.score_num
            self.clear()
            self.write(arg=f"YOUR SCORE : {SS}, HIGH SCORE : {self.high_score_num}", move=False, align=ALIGN, font=FONT)
            self.score_num = 0

            with open("D:\\100P\\day 20 -21\\data.txt", mode="w") as f:
                f.write(str(self.high_score_num))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
