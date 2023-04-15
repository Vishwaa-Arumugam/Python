# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
#
#
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# for (index, row) in student_data_frame.iterrows():
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter : row.code for (index, row) in data.iterrows()}
print(result)

should_continue = True
while should_continue:
    try:
        word = input("ENTER THE WORD : ").upper()
        answer = [result[letter] for letter in word]
        should_continue = False
    except KeyError:
        print("Sorry, only the letters in the alphabets please.")
    else:
        print(answer)

# another method with functions
# def function_call():
#     word = input("ENTER THE WORD : ").upper()
#     try:
#         answer = [result[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only the letters in the alphabets please.")
#         function_call()
#     else:
#         print(answer)
# function_call()