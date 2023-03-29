##Scope

enemies = 1 #global scope

def increase_enemies():
    enemies = 2 # local scope
    print(f"enemies inside functions : {enemies}")

increase_enemies()
print(f"enemies outside the function {enemies}")

game_level = 3
def abc():
    enemies = ["skeleton","zombie","alien"]
    if game_level < 5:
        new_enemy = enemies[0]
print(new_enemy)


modifying global scope

enemies = 1

def increase_enemies():
    print(f"enemies inside the finction : {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemis outside the finction : {enemies}")


#####################################FROM HERE THE ACTUAL DAY'S CHALANGE STARTS############################################


import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

msg ="""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
        """

def print_logo():
    print(logo)
    print(msg)
    num = random.randint(0,100)
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == "easy":
        total = 10
        print("You have 10 attempts remaining to guess the number.")
        find_num = True
        while find_num is True:
            user_choice = int(input("Make a guess: "))
            if total > 0:
                if (user_choice == num):
                    print(f"You got it, the answer is {num}")
                    find_num = False
                elif (user_choice > num):
                    print("Too high")
                    print("Guess again")
                    total = total - 1
                elif (user_choice < num):
                    print("Too low")
                    print("Guess again")
                    total = total - 1
            else:
                find_num = False

    elif choice == "hard":
        total = 5
        print("You have 5 attempts remaining to guess the number.")
        find_num_1 = True
        while find_num_1 is True:
            user_input = int(input("Make a guess: "))
            if total > 0:
                if user_input == num:
                    print(f"You got it, the answer is {num}")
                    find_num_1 = False
                elif (user_input > num):
                    print("Too high")
                    print("Guess again")
                    total = total - 1
                    if total == 0:
                        find_num_1 = False
                elif (user_input < num):
                    print("Too low")
                    print("Guess again")
                    total = total - 1
                    if total == 0:
                        find_num = False
            else:
                find_num_1 = False
print_logo()
