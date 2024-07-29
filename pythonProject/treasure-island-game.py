print("WELCOME TO TREASURE ISLAND\n")
print("You mission is to find the treasure.")
choice1=input("You're at a crossroad, where do you want to go? Type left or right.\n").lower()
if choice1=="left":
    choice2=input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.").lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if choice3=="red":
            print("It's a room full full of fire. GAME OVER ")
        elif choice3=="blue":
            print("You enter a room of beasts. GAME OVER ")
        elif choice3=="yellow":
            print("You found the treasure. YOU WIN!!")
        else:
            print("You've chosen a door that doesnt exist. GAME OVER ")
    else:
        print("You got attacked by an angry trout. GAME OVER ")

else:
    print("You fell into a hole. GAME OVER")
