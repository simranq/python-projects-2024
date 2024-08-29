import pandas
data = pandas.read_csv("nato_alphabet.csv")
# print(data.to_dict())
#TODO-1:CREATE A DICTIONARY in this format: {'A':"Alfa"...}
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)
#TODO-2: CREATE LIST OF THE PHONETIC CODE WORDS FROM A WORD THAT THE USER i/ps
user_input = input("ENTER A WORD: ").upper()
op_list=[phonetic_dict[letter] for letter in user_input]
print(op_list)
