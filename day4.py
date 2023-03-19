# import random

# random_integer = random.randint(100,200)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

#list
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
# "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
# "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
# "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
# "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
# "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america)

#nested list

# dd = ["name","age","college","town","state","country"]
# ds = ["vishwaa","20","ssn","apk","tn","ind"]

# nested = [dd,ds]
# print(nested[1][1]) #print 1 indexed list's 1 indexed element

# heads or tails

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
# import random
# #Write the rest of your code below this line 👇

# side = random.randint(0,1)
# if side == 1:
#     print("Heads")
# else:
#     print("Tails")

# pay money

# Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# length = len(names)
# print(names[random.randint(0, length - 1)] + " is going to buy the meal today!")

# treasure map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])
map [vertical - 1][horizontal - 1] = "X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# # rock paper scissor

# # Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# player = [rock,paper,scissors]
# computer = [rock,paper,scissors]

# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# print(player[choice])

# print("Computer chose:\n")
# computer_choice = random.randint(0,2)
# print(computer[computer_choice])

# if choice == computer_choice:
#     print("Its a draw")
# elif choice > 2 or computer_choice > 2:
#     print("Invalid input")
# elif choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and choice == 2:
#   print("You lose")
# elif computer_choice > choice:
#   print("You lose")
# elif choice > computer_choice:
#   print("You win!")