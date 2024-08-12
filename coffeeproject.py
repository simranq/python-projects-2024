#COFFEE MACHINE-COIN OPERATED
#COIN OPERATE (AMERICAN $)
#RESOURCES: 300ml WATER
#           200 ml MILK
#           100g Coffee
#3 hot flavours
#ESPRESSO-  price: 1.5
#           50ml water,
#           18g coffee
#           150ml milk
#LATTE-     price: 2
#            200ml water
#            24g coffee
#           150 ml milk
#CAPPUCINO-     price: 3
# 250 ml water
# 24g coffee
# 100 ml milk



#PROGRAM REQUIREMENTS
# I    Print report + the resources have to be dynamically keep on updating themselves
# II   Check if resources sufficient
# III  Process coins
# IV   Check if transaction successful?
# V    Make coffee


#1 Print logo and name
from coffeemachine_art import logo
print (logo)
print("WELCOME TO SIM'S CAFE")

#Content of menu & resources that are available
menu = {
    "espresso":{
            "ingredients":{
                "water":50,
                "coffee":18
            },
            "cost":1.5
               },
    "latte":{
            "ingredients":{
                "water":200,
                "coffee":24,
                "milk":150
            },
            "cost":2.5
    },
    "cappucino":{
            "ingredients":{
                "water":250,
                "coffee":24,
                "milk":100
            },
            "cost":3
    }
}


resources = {
    "water":300,
    "milk":200,
    "coffee":100
}
profit = 0
def is_resource_sufficient(order_ingredients):
    """Returns true when order is available to be made & false when it can't be made"""
    for item in order_ingredients:
        if order_ingredients [ item ] >= resources[item]:
            print(f"Sorry, there aren't enough {item}!")
            return False                            #resources aren't sufficient
        return True                                 #vice versa of above

#IN CENTS
# penny(1)<nickel(5)<dime(10)<quarter(25)
def process_coins() :
    """Returns the total coins that have been inserted"""
    print('Please insert coins: ')
    total = int(input('How many quarters? ')) * 0.25
    total += int(input('How many dimes? ')) * 0.10
    total += int(input('How many nickels? ')) * 0.50
    total += int(input('How many pennies? ')) * 0.01
    return total

def is_transaction_successful ( money_received , drink_cost ):
    """ Returns true if payment s successful & false if money is insufficient """
    if money_received >= drink_cost :
        change = round ( money_received - drink_cost , 2 )
        print(f"Here's your ${change} in change ")
        global profit
        profit += drink_cost    #if we write profit += drink_cost there will be an error 'unresolved reference profit'. This occurs due to profit being
                                # global var and drink_cost being in its local scope

        return True
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee ( drink_name , order_ingredients):
    """Deduct used up resources in real time"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} 🍵\n")
is_on = True

#2 Prompt the user for their choice

while is_on:
    choice = input("What would you like?  (ESPRESSO, LATTE, CAPPUCINO)\n").lower()
    if choice=="off":
        is_on = False

    elif choice =="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink['ingredients']):   #menu->choice->ingredients->...
            payment = process_coins()
            if is_transaction_successful (payment , drink['cost']) :
                make_coffee(choice , drink['ingredients'])
