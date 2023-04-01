# oops
# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen

# a = Turtle()
# print(a)
# a.shape("turtle")
# a.color("coral")
# a.forward(100)

# my_screen = Screen()
# print(Screen().canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squrtle","Charmander"])
table.add_column("Type",["Electric","water","Fire"])
table.align = "l"
print(table)