# # functions with outputs

# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "Please enter a valid input"

#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return (f"{formatted_f_name} {formatted_l_name}") # return is the end of the function

# print(format_name(input("ENTER YOUR FIRST NAME : "), input("ENTER YOUR LAST NAME : ")))

# #days in a month

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#         return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and month == 2:
#       return 29
#   return month_days[month - 1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# print(days_in_month(year, month))

# calculator
import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    n1 = float(input("ENTER THE 1ST NUMBER : "))
    for i in operation:
        print(i)

    should_continue = True
    while should_continue:
        operation_symbol = input("ENTER THE OPERATION : ")
        n2 = float(input("ENTER THE 2ND NUMBER : "))
        calculation = operation[operation_symbol]
        answer = calculation(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        choice = input(f"Type 'y' to calculate with {answer}, or 'n' to to start a new calculation : ")
        if choice == "y":
            n1 = answer
        elif choice == "n":
            should_continue = False
            os.system('cls')
            calculator()
        else:
            exit()
            

calculator()
