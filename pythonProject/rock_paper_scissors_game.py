import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
game_images = [rock, paper, scissors]
print("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS")
choice = int(input("You chose: "))

if choice >2 or choice <0:
    print("INVALID NUMBER ENTERED\nTry Again")
    
else :
    print(game_images[choice])
    
    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You Win!!")
    elif choice == 2 and computer_choice == 0:
        print("You Lose!!")
    elif choice > computer_choice :
        print ("You Win!!")
    else :
        print("You Lose!!")