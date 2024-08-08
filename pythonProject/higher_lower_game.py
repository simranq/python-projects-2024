import random

data = [
    {
        "name": "Dwayne Johnson",
        "profession": "Actor",
        "followers": 200
    },
    {
        "name": "Ariana Grande",
        "profession": "Singer",
        "followers": 250
    },
    {
        "name": "Leonardo DiCaprio",
        "profession": "Actor",
        "followers": 150
    },
    {
        "name": "Taylor Swift",
        "profession": "Singer",
        "followers": 220
    },
    {
        "name": "Cristiano Ronaldo",
        "profession": "Footballer",
        "followers": 300
    },
    {
        "name": "Beyoncé",
        "profession": "Singer",
        "followers": 240
    },
    {
        "name": "Narendra Modi",
        "profession": "Politician",
        "followers": 180
    },
    {
        "name": "Justin Bieber",
        "profession": "Singer",
        "followers": 210
    },
    {
        "name": "Kylie Jenner",
        "profession": "Businesswoman",
        "followers": 280
    },
    {
        "name": "Lionel Messi",
        "profession": "Footballer",
        "followers": 260
    },
    {
        "name": "Selena Gomez",
        "profession": "Singer",
        "followers": 230
    },
    {
        "name": "Kanye West",
        "profession": "Rapper",
        "followers": 190
    },
    {
        "name": "Lady Gaga",
        "profession": "Singer",
        "followers": 200
    },
    {
        "name": "Robert Downey Jr.",
        "profession": "Actor",
        "followers": 160
    },
    {
        "name": "Jennifer Lopez",
        "profession": "Singer",
        "followers": 180
    },
    {
        "name": "Nicki Minaj",
        "profession": "Rapper",
        "followers": 170
    },
    {
        "name": "Shakira",
        "profession": "Singer",
        "followers": 140
    },
    {
        "name": "Eminem",
        "profession": "Rapper",
        "followers": 130
    },
    {
        "name": "Rihanna",
        "profession": "Singer",
        "followers": 210
    },
    {
        "name": "Adele",
        "profession": "Singer",
        "followers": 140
    },
    {
        "name": "Chris Hemsworth",
        "profession": "Actor",
        "followers": 150
    },
    {
        "name": "Miley Cyrus",
        "profession": "Singer",
        "followers": 160
    },
    {
        "name": "Drake",
        "profession": "Rapper",
        "followers": 180
    },
    {
        "name": "Billie Eilish",
        "profession": "Singer",
        "followers": 170
    },
    {
        "name": "Virat Kohli",
        "profession": "Cricketer",
        "followers": 200
    },
    {
        "name": "Shawn Mendes",
        "profession": "Singer",
        "followers": 140
    },
    {
        "name": "Camila Cabello",
        "profession": "Singer",
        "followers": 130
    },
    {
        "name": "LeBron James",
        "profession": "Basketball Player",
        "followers": 120
    }
]

def check(num1,num2,guess):
    if num1 > num2 :
        return guess == "a"
    elif num1 < num2 :
        return guess == "b"

def game():
    print("\nHIGHER — LOWER GAME \n")
    score = 0
    account_b = random.choice(data)
    should_continue = True
    while should_continue :
        account_a = account_b
        account_b = random.choice(data )
        if account_a == account_b :
            account_b = random.choice(data)
        account_a_name = account_a["name"]
        account_a_prof = account_a["profession"] 
        print(f"Compare A:  {account_a_name}, {account_a_prof}")
        print("\nV/S\n")

        account_b_name  = account_b["name"]
        account_b_prof = account_b["profession"] 
        print(f"Against B: {account_b_name}, {account_b_prof}") 
        
        guess_it = input("Who has more followers according to you? Type 'A' or 'B':   ").lower()
        
        a_followers = account_a["followers"]
        b_followers = account_b["followers"]
    
        is_correct = check ( a_followers, b_followers , guess_it)
        if is_correct : 
            score += 1
            print(f"You're Correct\nCurrent Score: {score}")
            
        else:
            score -= 1
            print(f"Sorry you're wrong\nFinal Score: {score}")
            should_continue = False
            
game()
        
        