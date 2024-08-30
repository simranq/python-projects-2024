# Getting to know bout diff widgets
from tkinter import *
window = Tk()
window.title("PROJECT 27")
window.minsize(width=400,height=500)

#labels
my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.pack()

#buttons
def action():
    print("Do Something")
my_button = Button(text = "Click Here",command=action)
my_button.pack()

#entries
my_entry1 = Entry(width=30)
my_entry1.insert(END, string="Start Typing Dude.")
print(my_entry1.get())
my_entry1.pack()

#Text (textbox area)
my_box = Text(height=5,width=30)
my_box.focus()
my_box.insert(END,"Multi-line entry's fine example.")
print(my_box.get("1.0",END))
my_box.pack()

#Spinbox
def spinbox_used():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
my_spinbox.pack()

#Scale
def scale_used(value):
    print(value)
my_scale = Scale(from_=0,to=100,command=scale_used)
my_scale.pack()

#Checkbutton
def checkbutton_used():
    #prints 1 if on else 0
    print(checked_state.get())
#var to hold onto checked state, 0->0ff,1->On
checked_state = IntVar()
my_checkbutton = Checkbutton(text="Is On?",variable=checked_state)
checked_state.get()
my_checkbutton.pack()

#RadioButton
def radio_used():
    print(radio_state.get())
#var to hold onto which radio button is checked
radio_state = IntVar()
radio_button1 = Radiobutton(text="Option 1",value=1,variable=radio_state,command=radio_used)
radio_button2 = Radiobutton(text="Option 2",value=2,variable=radio_state,command=radio_used)
radio_button1.pack()
radio_button2.pack()

#ListBox
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))
my_listbox = Listbox(height=4)
fruits=["Avocado","Dragon Fruit","Papaya","Melon"]
for item in fruits:
    my_listbox.insert(fruits.index(item),item)
my_listbox.bind("<<ListboxSelect>>",listbox_used)
my_listbox.pack()

window.mainloop()