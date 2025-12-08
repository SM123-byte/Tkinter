from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Check Alert")
window.geometry('200x200')

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus Found!")

btn = Button(window, text= "Scan for Virus", command=msg)
btn.place(x=30, y=50)
btn.pack()

window.mainloop()