from tkinter import *

window = Tk()
window.title('Login Details')
window.geometry('400x400')

frame = Frame(master= window, height=200, width=360, bg="#d7e7ef")

lbl1= Label(frame, text= "Full Name", bg= "#2c8dcf", fg= 'white', width=12)
lbl2= Label(frame, text= "Email ID", bg= "#2c8dcf", fg= 'white', width=12)
lbl3= Label(frame, text= "Enter Password", bg= "#2c8dcf", fg= 'white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

textbox = Text(bg="#e3dcdc", fg='black')

# Function for displaying messages

def display():
    name = name_entry.get()
    greetmsg = "Hey " + name
    msg = "\n Congrats for your new account"
    textbox.insert(END, greetmsg)
    textbox.insert(END, msg)

btn = Button(text= "Create Account", command=display, bg="red")

# Placement of Widgets

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y= 140)
password_entry.place(x=150, y=140)

btn.place(x=130, y=210)
textbox.place(y=250)

window.mainloop()
