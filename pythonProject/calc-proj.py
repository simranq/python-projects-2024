#PROJ 2: TIP CALCULATOR
print("Welcome to the tip calculator!")
bill=float(input("\nWhat was the total bill? $ "))
tip=float(input("\nHow much %tip would you like to give? 10, 12, or 15? "))
ppl=float(input("\nHow many people are splitting the bill? "))
tip_as_percent=tip/100
total_tip=bill*tip_as_percent
total_bill=bill+total_tip
split=total_bill/ppl
a=round(split,2)
print("\nEach person should pay: $ ",a)

