from tkinter import *
from tkinter import messagebox

def calc():
    try:

        p = float(entry_principalamount.get())
        t = float(entry_timeperiod.get())
        r = float(entry_rateamount.get())

        si = (p * r * t) / 100

        ci = p * (pow((1 + r / 100), t)) - p

        label_si_result.config(text= f"Simple Interest: {si}")
        label_ci_result.config(text= f"Compound Interest: {ci}")

    except ValueError:
        messagebox.showerror("Please enter a valid input")

window = Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

lb1 = Label(window, text= "Principal Amount").pack()
entry_principalamount = Entry(window)
entry_principalamount.pack()

lb2 = Label(window, text= "Time Period / years").pack()
entry_timeperiod = Entry(window)
entry_timeperiod.pack()

lb3 = Label(window, text= "Rate Amount:").pack()
entry_rateamount = Entry(window)
entry_rateamount.pack()

btn = Button(window, text= "Calculate", command=calc, bg= "blue", fg= "black")
btn.pack()

label_si_result = Label(window, text="Simple Interest: 0.00")
label_si_result.pack()

label_ci_result = Label(window, text= "Compound Interest: 0.00")
label_ci_result.pack()

window.mainloop()