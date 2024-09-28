import math
from tkinter import Tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    #starts frm 00:00
    canvas.itemconfig(timer_text ,text= "00:00")
    #title_label "Timer"
    title_label.config(text="Timer")
    #reset tick
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #if it is 8th rep:
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    #if it is 2/4/6 rep:
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    # if it is the 1/3/5/7 rep:
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:  #strongly dynamic typed language
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        mark = ""
        for _ in range(work_sessions):
            mark += "✔"
        tick.config(text="✔")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")    #fact check:pomodoro means tomato in italian
window.minsize(width=500,height=500)
window.config(padx=100,pady=100,bg=YELLOW)

title_label = Label(text="Timer",font= (FONT_NAME,45),bg=YELLOW,fg = GREEN)
title_label.grid(row=0,column=1)

canvas = Canvas(width = 200 , height = 223 , bg = YELLOW , highlightthickness = 0)
tomato_img = PhotoImage (file = "tomato.png")
canvas.create_image(100,111,image=tomato_img)

timer_text = canvas.create_text(105,125,text = "00:00",fill="white", font = (FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",command=start_timer,font= (FONT_NAME,15),highlightthickness=0)
start_button.grid(row=2,column=0)

tick = Label(font=(FONT_NAME,35),fg=GREEN,bg=YELLOW)
tick.grid(row=2,column=1)

reset_button = Button(text="Reset",command= reset_timer,font= (FONT_NAME,15),highlightthickness=0)
reset_button.grid(row=2,column=2)

window.mainloop()
#--------------------WORKING OF REPS----------------------#
#25 min work
# 5 min break
# 25 min work
# 5 min break
# 25 min work
# 5 min break
# 20 min break