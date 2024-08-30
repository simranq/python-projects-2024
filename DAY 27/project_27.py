#---------------------------------------------------------------------------------
#                       MOVING ON TO OUR PROJECT FOR THE DAY
#---------------------------------------------------------------------------------
# pack<<place<<grid
from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config( text = f"{km}")
    
window = Tk()
window.title("mile To km Converter")
window.minsize(width=300,height=200)
window.config(padx=25,pady=25)

#   0th ROW:                          POSITION
#entry                                   0,1
miles_input = Entry(width = 5)
miles_input.grid(row=0,column=1)

#label
miles_label = Label(text="miles")            #0,2
miles_label.grid(row=0,column=2)

#   1st ROW
#label
is_equal_label = Label(text = "is equal to")
is_equal_label.grid(row=1,column=0)         #1,1

#label
km_result_label = Label(text = "0")             #1,1
km_result_label.grid(row=1,column=1)

#label
km_label = Label(text="km")                     #1,2
km_label.grid(row=1,column=2)
#   2nd ROW
#button
button = Button(text="CALCULATE",command=miles_to_km)
button.grid(row=2,column=1)

window.mainloop()