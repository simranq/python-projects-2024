import random
import hangman_words.py

chosen_word = random.choice(word_list)
print(f"Psst..the chosen word is {chosen_word}")
word_length = len(chosen_word)
display =[]
for _ in  chosen_word :
    display += "_"
print (display )

stages =["""
  +---+
  |   |
  O   |
 /|\\\  |
 / \\\  |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|\\\  |
 /    |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|\\\  |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""","""  
+---+
  |   |
      |
      |
      |
      |
=========
"""]
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: "). lower ()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter ==  guess:
            display[position] =  letter
            print(display)
    if guess not in chosen_word :
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose\nGAME OVER")
            
    if "_" not in display :
        end_of_game = True
        print("You Win.")
        
    print(stages[lives])
 