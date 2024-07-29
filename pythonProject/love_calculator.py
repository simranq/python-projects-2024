
a = input("Enter your name: ")
b = input("Enter your partner's name: ")
combined_name = a+b
lower = combined_name.lower()
t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
first_digit = t+r+u+e
l = lower.count("l")
o = lower.count("o")
v  = lower.count("v")
e  = lower.count("e")
second_digit = l+o+v+e
score = int(str(first_digit)+str(second_digit))
if score > 90 or score < 10:
    print(f"Your score  is {score}, you guys are like coke & mentos.")
elif score >= 40 and score<=50:
    print(f"Your score is {score}, .you .guys are alright together!")
else:
    print(f"Your score is {score}")

'''
we can use random module as:
import random
love_score = random.randint(1,100)
print(f"Your love score is {love_score}%")
'''