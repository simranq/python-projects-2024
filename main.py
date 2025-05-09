from tkinter import *
from tkinter import messagebox
import random
from random import choice,randint, shuffle
import pyperclip


#----------------------------------------------------------------------------------------------------------------------
#                                                        PASSWORD GENERATOR
#----------------------------------------------------------------------------------------------------------------------

def generate_password():
    password_entry.delete(0,END)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols =['!','@','#','$','%','^','*','&','(',')','-','_','+','{','}','[',']','\',','.','<','>','?','=','~']

    password_letters = [random.choice(letters) for _ in range(randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers +password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

#----------------------------------------------------------------------------------------------------------------------
#                                                           SAVE PASSWORD
#----------------------------------------------------------------------------------------------------------------------
def save_credentials():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oopsie!!",message="Please do not leave any field empty!")
    # messagebox.showinfo(title="title",message="Added")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are te details entered:\nWebsite: {website}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


#----------------------------------------------------------------------------------------------------------------------
#                                                           UI SETUP
#----------------------------------------------------------------------------------------------------------------------

window = Tk()
window.title("Password Manager")
# window.minsize(width=500 , height=500)
window.config(padx=60,pady=60,bg="#FFF")

canvas = Canvas(width=250, height=200,bd=0,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(120,115,image=logo_img)
canvas.grid(row= 0,column= 1)

# labels
website_label =Label(text="Website: ")
website_label.grid(row= 1,column= 0)

username_label =Label(text="Email/Username: ")
username_label.grid(row= 2,column= 0)

password_label =Label(text="Password: ")
password_label.grid(row= 3,column= 0)

# entries

website_entry = Entry(width=60)
website_entry.grid(row= 1,column= 1,columnspan= 2)
website_entry.focus() #cursor points here when launched

username_entry = Entry(width=60)
username_entry.grid(row= 2,column= 1,columnspan= 2)
username_entry.insert(END,'qsimran08@gmail.com')

password_entry = Entry(width=42)
password_entry.grid(row= 3,column= 1)

# buttons
#----------------------------------------------------
#generate password button
generate_password_button =Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row= 3, column= 2)

# add button
add_button =Button(text="Add",width=50,command=save_credentials)
add_button.grid(row= 4, column= 1,columnspan=2)
#----------------------------------------------------
window.mainloop()