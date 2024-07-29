import random
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7' ,'8', '9', '0']
symbols = ['~' , '!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '<' , '>' , '/' , '?' , '{' ,'}' ,'[' , ']' , ',' , '.']


print("WELCOME TO THE PYPASSWORD GENERATOR")
nr_letters = int(input("How many letters would you like in your password?"))
.nr_symbols = int(input("How many symbols would you like in your password?"))
nr_numbers = int(input("How many numbers would you like in your password?"))

pswd_list = []
for char in range(1,nr_letters + 1) :
     pswd_list.append(random.choice(letters))

for char in range(1,nr_symbols + 1) :
     pswd_list.append(random.choice(symbols))

for char in range(1,nr_numbers+ 1) :
     pswd_list.append(random.choice(numbers))
#rint(pswd_list)

random.shuffle(pswd_list)
#print(pswd_list)

password = ""
for i in pswd_list :
    password += i

print(f"Your generated password is: {password}")
