print("QUALIFICATION FORM\n#NOTE: HEIGHT MEASUREMENTS IN cm\n")
height=int(input("Enter your height: "))
if (height>=120):
    print("You are eligible to ride.")
    age = int(input("\nEnter your age: "))
    if (age<=12):
            bill=5
            print("\nChild tickets are $5.")
    elif (age<18):
            bill=7
            print("Teen tickets are $7.")
    else:
            bill=12
            print("Adult tickets are $12.")
    wants_photos=input("Do you wanna take photos? Y / N  ")
    if (wants_photos=="Y"):
        bill+=3
    print(f"\nTotal bill is ${bill}")
else:
    print("Not eligible to ride")
