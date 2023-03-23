# #function with arguments and inputs , ceaser cipher

# #simple function
# def greet():
#     print("HI")
#     print("HELLO")
#     print("HRU")
# greet()

# #functions with inputs

# def greet_with_name(name): #--> here name is called as parameter and the value added to the parameter name is called as argument
#     print(f"HI {name}")
#     print(f"HELLO {name}")
#     print(f"HRU {name}")
# greet_with_name("vishwaa")

# def greet_with(name,location):
#     print(f"HELLO {name}")
#     print(f"What is it like in {location}")
# greet_with(location="apk",name="vishwaa")

# #wall painting
# import math

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# def paint_calc(height=test_h, width=test_w, cover=coverage):
#     t = math.ceil((test_h*test_w)/5)
#     print(f"You'll need {t} cans of paint.")
# paint_calc()

# #prime number or not 

# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")



# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


#ceaser cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, no_shift, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                new_position = position + shift
            elif cipher_direction == "decode":
                new_position = position - no_shift
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

to_continue = True
while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(start_text=text,no_shift=shift,cipher_direction=direction)
    result = input("Type 'Yes' if you want to continue. otherwise type 'no'")
    if result == 'no' or result == 'No':
        to_continue = False
        print("Thank you")