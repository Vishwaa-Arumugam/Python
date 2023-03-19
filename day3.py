#PIZZA ORDER
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    elif add_pepperoni == "N":
        bill += 0
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill  += 0

elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    elif add_pepperoni == "N":
        bill += 0
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill  += 0
    

elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    elif add_pepperoni == "N":
        bill += 0
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill  += 0
    

print(f"Your final bill is: ${bill}.")

#love calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score = 0
res = name1 + name2
lower = res.lower()
t = lower.count("t")
score += t
r = lower.count("r")
score += r
u = lower.count("u")
score += u
e = lower.count("e")
score += e
score_1 = 0
l = lower.count("l")
score_1 += l
o = lower.count("o")
score_1 += o
v = lower.count("v")
score_1 += v
e = lower.count("e")
score_1 += e
total = int(str(score) + str(score_1))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")

elif total>= 40 and total<= 50:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"Your score is {total}")

#treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")