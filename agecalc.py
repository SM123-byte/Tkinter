from tkinter import *
from datetime import date

# Fetch the current date for exact calculation

def calc():
    today = date.today()

    birth_day = int(entry2.get())
    birth_month = int(entry3.get())
    birth_year = int(entry4.get())

    age = today.year - birth_year
    
    if (today.month < birth_month) or (today.month == birth_month and today.day < birth_day):
        age -= 1 

    name = entry1.get()
    result_text = f"Hello {name}! You are {age} years old!"

    result_label.config(text=result_text)

window = Tk()
window.title('Age Calculator App')
window.geometry('400x400')

lbl1 = Label(text= "Enter Name: ", bg= "#62C0F0")
entry1 = Entry(window, width=20)

lbl2 = Label(text= "Enter Date of your birthday (DD): ", bg= "#62C0F0")
entry2 = Entry(window, width=20)

lbl3 = Label(text= "Enter the month you were born on (MM): ", bg= "#62C0F0")
entry3 = Entry(window, width=20)

lbl4 = Label(text= "Enter the year you were born on (YYYY): ", bg= "#62C0F0")
entry4 = Entry(window, width=20)

btn = Button(window, text= "Calculate Age", bg="#73EB77", fg= "aqua", command=calc)

result_label = Label(window, text="", bg="#FFFFFF", wraplength=380)


lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
lbl3.pack()
entry3.pack()
lbl4.pack()
entry4.pack()
btn.pack()
result_label.pack()

window.mainloop()