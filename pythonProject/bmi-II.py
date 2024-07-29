'''THIS IS A BMI CALCULATOR
    Also, it is an upgraded version of the previous "bmi.py" file with certain suggestions
'''
wt=int(input("WELCOME TO SIM'S BMI CALCULATOR\nNOTE: Weight should be in kg & height in metres\nPlease enter your weight: "))
ht=float((input("\nPlease enter your height: ")))
bmi=int(wt/(ht**2))
if (bmi<19):
    print(f"Your BMI score is: {bmi}, you are slightly UNDERWEIGHT.")
elif (bmi==22):
    print(f"Your BMI score is: {bmi}, you are perfectly NORMAL. ")
elif (29>bmi>22):
    print(f"Your BMI score is: {bmi}, you are slightly OVERWEIGHT.  ")
elif (37>bmi>29):
    print(f"Your BMI score is: {bmi}, you are OBESE. ")
else:
    print(f"Your BMI score is: {bmi}, you are clinically OBESE. ")
