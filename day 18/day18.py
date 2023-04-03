# ######## Challenge 1 - Draw a Square ############
import turtle as t
import random
#
aamai = t.Turtle()
#
# for _ in range(4):
#     aamai.forward(100)
#     aamai.left(90)
#
# ########### Challenge 2 - Draw a Dashed Line ########
# for _ in range(15):
#     aamai.forward(10)
#     aamai.penup()
#     aamai.forward(10)
#     aamai.pendown()

########### Challenge 3 - Draw Shapes ########

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         aamai.forward(100)
#         aamai.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     aamai.color(random.choice(colours))
#     draw_shape(shape_side_n)

# ########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
# directions = [0, 90, 180, 270]
# aamai.pensize(15)
# aamai.speed("fastest")
#
# for _ in range(200):
#     aamai.color(random.choice(colours))
#     aamai.forward(30)
#     aamai.setheading(random.choice(directions))
#
# ########### Challenge 5 - Spirograph ########
#
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    aamai.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        aamai.color(random_color())
        aamai.circle(100)
        aamai.setheading(aamai.heading() + size_of_gap)

draw_spirograph(5)
