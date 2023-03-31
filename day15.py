# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
w = resources["water"]
m = resources["milk"]
c = resources["coffee"]
r = 0.00

def report():
    return print(f"Water : {w}ml \nMilk : {m}ml \nCoffee : {c}ml \nMoney : {r}$")

def coffee():
    print("please enter coins.")
    quaters = int(input("Please enter quaters?: "))
    dimes = int(input("Please enter dimes?: "))
    nickles  = int(input("Please enter nickles?: "))
    pennies = int(input("Please enter pennies?: "))
    total = (quaters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    if total >= (MENU[choice]["cost"]):
        diff = total - (MENU[choice]["cost"])
        return f"Here's your {'%.2f' % diff}$ change"
    else:
        print("Sorry, that's not enough money. Money refunded")
        exit()

def buy():
    water = MENU[choice]["ingredients"]["water"]
    coffee = MENU[choice]["ingredients"]["coffee"]
    milk = MENU[choice]["ingredients"]["milk"]
    final_water = w - water
    final_milk = m - milk
    final_coffee = c - coffee
    return print(f"Water : {final_water}ml \nMilk : {final_milk}ml \nCoffee : {final_coffee}ml")

should_continue = True
while should_continue is True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if "report" in choice:
        report()
    elif "espresso" in choice:
        if resources["water"] >= 50 and resources["coffee"] >=18:
            print(coffee())
            print(f"Here's your {choice} ☕️. Enjoy!")
            r += (MENU[choice]["cost"])
            buy()
        else:
            print("Sorry, there is not enough water")
            should_continue = False
    elif "latte" in choice:
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            print(coffee())
            print(f"Here's your {choice} ☕️. Enjoy!")
            r += (MENU[choice]["cost"])
            buy()
        else:
            print("Sorry, there is not enough water")
            should_continue = False
    elif "cappuccino" in  choice:
        if resources["water"] >= 250 and resources["milk"] >=100 and resources["coffee"] >= 24:
            print(coffee())
            print(f"Here's your {choice} ☕️. Enjoy!")
            r += (MENU[choice]["cost"])
            buy()
        else:
            print("Sorry, there is not enough water")
            should_continue = False
    elif "off" in choice:
        should_continue = False
    

