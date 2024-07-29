print("Thank You for choosing PYTHON PIZZA DELIVERIES! ")
size = input("\nWhat else pizza is you want? S M L    ")
add_chicken = input("\nDo you wanna add chicken? Y / N    ")
add_cheese = input("\nDo you wanna add extra cheese? Y / N    ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_chicken == "Y":
    if size == "S":
            bill += 2
    else:
            bill += 3
if add_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")
