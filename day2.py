# print("hello"[-1])

# s = "Abbey Road"
# print(s[4] + s[7])

# num_char = len(input("ENTER YPUR NAME : "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")

print("Welcome to the tip calculator")
a = float(input("What was the total bill? $"))
b = int(input("How much tip would you like to give? 10, 12 or 15? "))
c = int(input("How many people to split the bill?"))
tip_1 = b/100
total_tip = a * tip_1
bill = a + total_tip
bill_p = bill / c
final = round(bill_p, 2)
final = "{:.2f}".format(bill_p)
print(f"Each person should pay: ${final}")