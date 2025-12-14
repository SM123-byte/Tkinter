from tkinter import *
from tkinter import messagebox

def calc():

    try:
        inches = float(inches_entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    
    except ValueError:
        messagebox.showerror("Invalid input! Please enter a numerical value")

window = Tk()
window.title('Length Converter App')
window.geometry('300x150')

inches_label = Label(window, text="Enter inches:")
inches_label.pack(pady=5)

inches_entry = Entry(window, width=10)
inches_entry.pack()

calculate_button = Button(window, text= "Convert", command=calc)
calculate_button.pack(pady=10)

result_label = Label(window, text= "Result: --cm")
result_label.pack(pady=5)

window.mainloop()