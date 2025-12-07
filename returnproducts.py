from tkinter import * 
import math 


    
window = Tk()
window.title('Getting started with Widgets')
window.geometry('400x300')

lbl = Label(text= "Hello! This application will take two numbers and give you the product of it!", fg= "White", bg= "#1555A3", height=2, width= 300, wraplength=350)

first_lbl = Label(text= "First Number", bg= "#E7EDF0")
entry_num1 = Entry(window, width=20)

second_lbl = Label(text= "Second Number", bg= "#E7EDF0")
entry_num2 = Entry(window, width=20)

btn = Button(window, text= "Calculate", bg="#4CAF50", fg= "white")

result_var = StringVar()
result_var.set("Enter values and press Calculate")

result_label = Label(window, textvariable=result_var, bg= "#E7EDF0")

def calc():
        
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        product = num1 * num2
        result_var.set(f"Product: {product}")

    except ValueError:

        result_var.set("Error: Invalid Input")

btn.config(command=calc)

lbl.pack()
first_lbl.pack()
entry_num1.pack()
second_lbl.pack()
entry_num2.pack()
btn.pack()
result_label.pack()

window.mainloop()