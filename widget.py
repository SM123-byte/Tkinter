from tkinter import *
from datetime import date

window = Tk()

window.title('Getting started with Widget Window')
window.geometry('400x300')

lbl = Label(text= "Hey there!", fg= "White", bg= "#1555A3", height=1, width= 300)

name_lbl = Label(text= "Full Name", bg= "#2191DB")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome To The Application!\n Today's date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
btn = Button(text= "Begin", command= display, height= 1, bg="#080101", fg= "Black")

# Augnise all widgets in the window

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()