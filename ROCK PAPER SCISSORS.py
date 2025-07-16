import tkinter as tk
import random

# Game logic
choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize scores
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n{result}")
    score_label.config(text=f"Score\nYou: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score\nYou: 0 | Computer: 0")

# GUI setup
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x400")
window.config(bg="lightblue")

title_label = tk.Label(window, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

result_label = tk.Label(window, text="Make your move!", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

score_label = tk.Label(window, text="Score\nYou: 0 | Computer: 0", font=("Arial", 12), bg="lightblue")
score_label.pack(pady=20)

reset_btn = tk.Button(window, text="Play Again", font=("Arial", 12), command=reset_game)
reset_btn.pack()

window.mainloop()