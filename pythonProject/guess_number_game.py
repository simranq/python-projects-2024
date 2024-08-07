import random        
import art.py
easy_level_attempts = 10
hard_level_attempts = 5

def check (guess , ans , turns) :
    if guess == ans:
        print("You Win")
                
    elif guess < ans :
         print("Too Low Guess Again")
         return turns - 1
                
    else :
        print("Too High. Guess Again")
        return turns - 1
        
def set_difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard':  ")
    if level == "easy":
        return easy_level_attempts
        
    elif level == "hard":
        return hard_level_attempts
      
    else :
        print ("INVALID INPUT \nTRY AGAIN")
        
    
def guess_game():
    print(logo)
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")
    ans = random.randint(1,100)
    turns = set_difficulty_level()
    
    if turns == 0:
        print ("You're out of guesses. You lose")
        return 
    print(f"Psst.. the correct guess should be {ans}")
    guess = 0
    while guess != ans :
        print (f"You've {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:  "))
        
        turns = check(guess,ans,turns)
        if turns == 0:
            print ("You are out of turns. You Lose")
            return 
guess_game()   

        
        
        
        
        
        
        
        
        