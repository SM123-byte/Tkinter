from tkinter import *
from tkinter import messagebox

def password_checker():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text= "Strength: Please Enter A Password", fg= "black")
    elif length < 6:
        result_label.config(text= "Strength: Weak - Too Short", fg= "red")
    elif length < 10:
        result_label.config(text= "Strength: Medium - Acceptable", fg= "orange")
    else:
        result_label.config(text= "Strength: Strong - Excellent", fg= "green")

window = Tk()
window.title("Password Checker App")
window.geometry("400x300")

lb1 = Label(window, text= "Enter Password:").pack()

password_entry = Entry(window, show= "*", width= 30)
password_entry.pack()

btn1 = Button(window, text= "Check Strength", command=password_checker, fg= "black")
btn1.pack()

result_label = Label(window, text= "Strength: ")
result_label.pack()

window.mainloop()