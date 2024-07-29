#This is a random name generator using lists in python
import random
names = ['Angela','John','Jack','Stacy']
num_items = len(names)
random_choice = random.randint(0 , num_items-1)
payer = names[random_choice]
print(" Meal is on "+ payer+"!!")