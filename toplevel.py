from tkinter import *

window = Tk()
window.title("Main")
window.geometry("300x300")

def toplevel():
    
    top = Toplevel()
    top.title("Top Window")
    top.geometry("200x100")
    l2 = Label(top, text= "This is a top level window!")
    l2.pack()
    top.mainloop()

l1 = Label(window, text= "This is the main window!")
btn = Button(window, text= "Click Me to open another window", command=toplevel)

l1.pack()
btn.pack()

window.mainloop()