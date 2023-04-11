#list comprehension

# syntax : new_list = [new_item for item in list if test]

numbers = [1,2,3]

new_num = [i + 1 for i in numbers]

print(new_num)


name = "Vishwaa"

new_list = [letter for letter in name]

print(new_list)


print([i * 2 for i in range(1, 5)])


names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_name = [item for item in names if len(item) <= 4]
print(short_name)
long_name = [item.upper() for item in names if len(item) > 4]
print(long_name)


# dictionary comprehension

#syntax : new_dict = {new_key:new_vlaue for (key,value) in dict.items() if test}

import random

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passesd_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passesd_students)