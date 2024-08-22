#import re
PLACEHOLDER = "[name]"
with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()#returns file content as a list
    #print(names)
with open("./input/letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip() # will strip off unused whitespace
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f"./output/ready_to_send/letter_for_{stripped_name}.docx" , mode = "w") as completed_letter:
            completed_letter.write(new_letter)