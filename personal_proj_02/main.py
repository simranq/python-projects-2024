from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
#-----------------------------------------PANDAS SETUP----------------------------------------------

try:
    data = pandas.read_csv('data/terms_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/data.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient="records")

#-----------------------------------------FUNCTIONS------------------------------------------------

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Term", fill="black")
    canvas.itemconfig(card_term, text=current_card["Term"], fill="black")
#below stmt fixed the bug
    canvas.itemconfig(card_def, text="", fill="white")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Definition", fill="white")
    canvas.itemconfig(card_term, text="", fill="white")
    canvas.itemconfig(card_def, text=current_card["Definition"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/terms_to_learn.csv", index=False)

    next_card()

#------------------------------------------GUI SETUP------------------------------------------------
window = Tk()
window.title("Flash Card")
window.config ( padx = 50 , pady= 50 , bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image = card_front_img)

card_title = canvas.create_text(400,140,text="Title", font=("Arial",40,"italic"))
card_term = canvas.create_text(400, 250, text="word", font=("Arial", 40, "bold"))
card_def = canvas.create_text(400, 350, font=("Arial", 25, "bold"), width=350)

canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan = 2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image= cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image= check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

next_card()
window.mainloop()