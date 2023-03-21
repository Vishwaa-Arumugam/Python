# fruits = ["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)

#highest score
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# print(student_scores)
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highest_score = 0
# for s in student_scores:
#     if s > highest_score:
#         highest_score = s
# print(f"The highest score in the class is: {highest_score}")



# # student heights
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# height = 0
# for h in  student_heights:
#     height += h

# stud = 0
# for s in student_heights:
#     stud += 1

# print(round(height / stud))


for i in range(1,11,2):
    print(i)

total = 0
for i in range(1,101):
    total += i
print(total)

# sum of all even numbers from1 to 100
#Write your code below this row 👇
total = 0
for i in range(2,101,2):
    # print(i)
    total += i
print(total)

# fizz buzz
#Write your code below this row 👇

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

#password generator
# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for c in range(1, nr_letters + 1):
    password += random.choice(letters)
for s in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for n in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []

for c in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for s in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for n in range(1, nr_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)


new =""
for i in password:
    new += i

print(f"Your password is : {new}")


