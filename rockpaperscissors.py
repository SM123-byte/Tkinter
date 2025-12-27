from tkinter import *
from tkinter import messagebox
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = f"It's a tie: You played {choice}; computer played {computer_choice}"
    elif (choice == "Rock" and computer_choice == "Scissors") or (choice == "Scissors" and computer_choice == "Paper") or (choice == "Paper" and computer_choice == "Rock"):
        result = f"You won!: You played {choice}; computer played {computer_choice}"
    else:
        result = f"Sorry! You lost!: You played {choice}; computer played {computer_choice}"

    result_label.config(text=result)

window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")

instruct_label = Label(window, text= "Choose your move")
instruct_label.pack(pady=20)

Button(window, text= "Rock", width=15, command= lambda: play("Rock")).pack(pady=5)
Button(window, text= "Paper", width=15, command= lambda: play("Paper")).pack(pady=5)
Button(window, text= "Scissors", width=15, command= lambda: play("Scissors")).pack(pady=5)

result_label = Label(window, text= "")
result_label.pack(pady=30)

window.mainloop()