import random

print("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS")
choice = int(input("You chose: "))
computer_choice = random.randint(0,2)

print(f"Computer chose: {computer_choice}")

if choice == 0 and computer_choice == 0:
    print("It's a TIE!!")
elif choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 0 and computer_choice == 2:
    print("You win!")
elif choice == 1 and computer_choice ==0:
    print("You win!")
elif choice == 1 and computer_choice == 1:
    print("It's a TIE!!")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 2:
    print("It's a TIE!!")
elif choice == 2 and computer_choice == 0:
    print("You lose")
elif choice == 2 and computer_choice == 1:
    print("You win!")
else :
    print("INVALID NO. ENTERED\n RETRY")
