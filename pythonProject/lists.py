fruits = ["apple", "banana", "orange"]
fruits[1] = "Jamun"
print(fruits[1])

fruits.append("melon")
print(fruits)

fruits.extend(["avocado","pear","cherry"])
print(fruits)

veggies = ["kale", "spinach","potatoes"]
healthy = [fruits + veggies]
print(healthy)