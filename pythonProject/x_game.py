line1 =["1 "," 2"," 3"]
line2 =[" 4","5 "," 6"]
line3 =["7 ","8 "," 9"]

print("Hiding your treasure! X marks the spot.")
print(f"{line1}\n{line2}\n{line3}")
map = [line1 , line2 , line3]
position = input()#where you wanna put the treasure
letter = position.lower()
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
