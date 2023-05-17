from logo import logo
print(logo)
coffee_type = {
   "espresso":{
        "ingredients":{
            "espresso": 25,
            "water": 30,
        },
        "cost": 1.5
    },
    "cappuccino":{
        "ingredients":{
            "espresso": 25,
            "milk": 150,
        },
        "cost": 2
    },
    "americano":{
        "ingredients":{
            "espresso": 30,
            "milk": 240,
            "water":50,
            "sugar": 50
        },
        "cost": 2.5
    }
}
available_ingredients = {
    "water": 500,
    "sugar": 400,
    "espresso": 1000,
    "milk": 500
}
profit = 0
def check_ingredients(order_ingredients):
    for item in order_ingredients:
        if available_ingredients[item] >= order_ingredients[item]:
            available_ingredients[item] -= order_ingredients[item]
        else:
            print(f"There have not suffient {item}")
            return False
    return True
def check_payment(payment, drink_cost):
    if payment > drink_cost:
        
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
    else:
        print("You didn't give sufficient amount for the coffee.")
        print(f"We have returned ${payment}.")
        return False
    return True
def make_coffee(drink_name, drink_cost):
    global profit
    profit += drink_cost
    print(f"Here is your {drink_name}. Enjoy!")
is_on = True
while is_on:
    choice = input("Please choose the type of coffe like espresso, cappuccino, americano: ")
    if choice =="off":
        is_on = False
    elif choice == "report":
        print(available_ingredients)
        print(f"Total profit: ${profit}")
    else:
        payment = int(input("Please pay for your item: "))
        drink = coffee_type[choice]
        if check_ingredients(drink["ingredients"]):
            if check_payment(payment,drink["cost"]):
                make_coffee(choice,drink["cost"])
