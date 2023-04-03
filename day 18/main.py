# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
aamai = turtle.Turtle()
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

no_of_dots = 100

aamai.speed("fastest")
aamai.setheading(225)
aamai.penup()
aamai.forward(300)
aamai.setheading(0)

def dot():
    for _ in range(10):
        aamai.dot(20, random.choice(color_list))
        aamai.forward(50)

for _ in range(10):
    dot()
    aamai.left(90)
    aamai.forward(50)
    aamai.left(90)
    aamai.forward(500)
    aamai.left(180)

screen = turtle.Screen()
screen.exitonclick()