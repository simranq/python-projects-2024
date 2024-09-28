import pandas as pd

data = pd.read_csv("nato_alphabets.csv")

# print(data.to_dict())

#TODO-1:CREATE A DICTIONARY in this format: {'A':"Alfa"...}

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

#TODO-2: CREATE LIST OF THE PHONETIC CODE WORDS FROM A WORD THAT THE USER i/ps

def generate_phonetic():
    word = input("ENTER A WORD: ").upper()
    try:
        op_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Oopsie! Only letters in alphabets are allowed.")
        generate_phonetic()

    else:
        print(op_list)

generate_phonetic()
