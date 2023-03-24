# #python dictionaries
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again."
# }

# print(programming_dictionary["Function"])

# programming_dictionary = {}

# #grading system
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# #TODO-2: Write your code below to add the grades to student_grades.👇
# for i in student_scores:
#     score = student_scores[i]
#     if score >= 91:
#         student_grades[i] = "Outstanding"
#     elif score >= 81 and score <= 90:
#         student_grades[i] = "Exceeds Expectations"
#     elif score >= 71 and score <= 80:
#         student_grades[i] = "Acceptable"
#     else:
#         student_grades[i] = "Fail"  
# print(student_grades)

# # 🚨 Don't change the code below 👇
# # print(student_grades)

# #nested dictionaries

# capitals = {
#     "India" : "Delhi",
#     "Britain" : "England"
# }

# nesting a list in dict

# travel_log = {
#     "France" : { "City_visited" : ["paris", "Lille", "Dijon"], "Total_visited" : 12 } ,
#     "germany" : {"city_visited" : ["berlin", "hamburg", "stuttgart"],"Total_visited" : 7}
# }

# # nesting a dic in list

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited, no_of_times , cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = no_of_times
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# blind auction
import os
from time import sleep
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to secret auction program")

bidding_details = {}

def details():
    name = input("ENTER THE NAME : ")
    price = int(input("ENTER YOUR BIDDING PRICE : "))
    bidding_details[name] = price
    choice = input("ARE THERE ANY OTHER BIDDERS(YES, NO) : ")
    if choice == "yes":
        os.system('cls')
        details()
    elif choice == "no":
        # print(bidding_details)
        pass
details()


high = 0
winner = ""
for i in bidding_details:
    bid_amount = bidding_details[i]
    if bid_amount > high:
        high = bid_amount
    winner = i
print(f"The winner is {i} with the highest bidd of {high}")







