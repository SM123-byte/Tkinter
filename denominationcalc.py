from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denomination Calculator")
window.geometry("650x400")
window.configure( bg='light blue')

upload = Image.open("/Users/swagatmohanty/Documents/Python/Tkinter/app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
lbl1 = Label(window, image= image, bg= "light blue")
lbl1.place(x=180, y= 20)

lbl2 = Label(window, text= "Welcome to the Denomination Calculator", bg= "light blue")
lbl2.place(relx= 0.5,y= 340, anchor= CENTER)

def msg():
    msgbox = messagebox.showinfo("Alert", "Do you want to calculate the denomination amount?")
    if msgbox == "ok":
        topwin()

btn1 = Button(window, text= "Let's get started!", command=msg, bg= 'brown', fg= 'black')
btn1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("600x350+50+50")
    l1 = Label(top, text= "Enter total amount!", bg= 'light grey')
    entry1 = Entry(top)
    l2 = Label(top, text= "Here are notes of each denomination", bg= 'light grey')
    l3 = Label(top, text= "100", bg= 'light grey')
    l4 = Label(top, text= "50", bg= 'light grey')
    l5 = Label(top, text= "1", bg= 'light grey')
    entry2 = Entry(top)
    entry3 = Entry(top)
    entry4 = Entry(top)

    def calc():
        try: 
            global amount
            amount = int(entry1.get())
            n1 = amount//100
            amount %= 100
            n2 = amount//50
            amount %= 50
            n3 = amount//1
            amount %= 1
            
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry2.insert(END, str(n1))
            entry3.insert(END, str(n2))
            entry4.insert(END, str(n3))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            
    btn2 = Button(top, text= "Calculate", command=calc, bg= "brown", fg= "black")
    
    l1.place(x=230, y=50)
    l2.place(x=140, y=170)
    l3.place(x=180, y=200)
    l4.place(x=180, y=230)
    l5.place(x=180, y=260)

    entry1.place(x= 200 , y= 80)
    entry2.place(x= 270, y= 200)
    entry3.place(x= 270, y= 230)
    entry4.place(x= 270 , y= 260)
    btn2.place(x= 240, y= 120)

    top.mainloop()

window.mainloop()