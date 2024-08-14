import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a random number
def generate_number():
    return random.randint(1, 100)

# Function to check the user's guess
def check_guess():
    try:
        guess = int(entry_guess.get())
        global attempts, low, high

        if guess < low or guess > high:
            messagebox.showinfo("Invalid Input", f"Please enter a number within the range {low}-{high}.")
            return
        
        attempts += 1
        
        if guess < number_to_guess:
            label_feedback.config(text="Too low! Try again.", fg="blue")
            low = guess + 1 # Narrow down the range
            update_range()
        elif guess > number_to_guess:
            label_feedback.config(text="Too high! Try again.", fg="red")
            high = guess - 1 # Narrow down the range
            update_range()
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {number_to_guess} correctly in {attempts} attempts.")
            reset_game()

    except ValueError:
        messagebox.showinfo("Invalid Input", "Please enter a valid integer.")

# Function to update the range
def update_range():
    label_range.config(text=f"Enter your guess between {low} and {high}:")

# Function to reset the game
def reset_game():
    global number_to_guess, attempts, low, high
    number_to_guess = generate_number()
    attempts = 0
    low = 1
    high = 100
    label_feedback.config(text="")
    entry_guess.delete(0, tk.END)
    update_range()

# Initialize the game
number_to_guess = generate_number()
attempts = 0
low = 1
high = 100

# Set up the main application window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x300")
root.configure(bg="#F8F9FA")

# Display instructions
label_instructions = tk.Label(root, text="Guess the Number Game!", font=("Arial", 16, "bold"), bg="#FFC107", fg="white", padx=20, pady=10)
label_instructions.pack(pady=10)

# Display the current range
label_range = tk.Label(root, text=f"Enter your guess between {low} and {high}:", font=("Arial", 12), bg="#F8F9FA", fg="#495057")
label_range.pack(pady=5)

# Entry box for the user's guess
entry_guess = tk.Entry(root, width=10, font=("Arial", 12), bd=3, relief="ridge")
entry_guess.pack(pady=10)

# Feedback Label
label_feedback = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#F8F9FA", fg="#6C757D")
label_feedback.pack(pady=10)

# Bind the Enter key to check the guess
entry_guess.bind("<Return>", lambda event: check_guess())

# Start the Tkinter event loop
root.mainloop()
