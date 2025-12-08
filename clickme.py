from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry('200x200')

def event_handler(event):
    print(event.char)

window.bind("<Key>", event_handler)

def click(event):
    print("\n Button was clicked!")

btn = Button(text="Click me")
btn.pack()

btn.bind("<Button-1>", click)

window.mainloop()