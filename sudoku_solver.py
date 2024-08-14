import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True

def read_board():
    board = []
    for row in range(9):
        current_row = []
        for col in range(9):
            val = entries[row][col].get()
            current_row.append(int(val) if val else 0)
        board.append(current_row)
    return board

def display_solution(board):
    for row in range(9):
        for col in range(9):
            if entries[row][col].get() == "":
                entries[row][col].insert(tk.END, str(board[row][col]))
                entries[row][col].config(fg="blue", font=("Arial", 18, "bold"))

def solve():
    board = read_board()
    if solve_sudoku(board):
        display_solution(board)
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists!")

def clear_board():
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].config(fg="black", font=("Arial", 18))

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg="#F0F0F0")

# Add Instructions at the top
instructions = tk.Label(
    root, 
    text="Enter the known numbers in the grid and click 'Solve' to complete the Sudoku puzzle.\nClick 'Clear' to reset the grid.", 
    font=("Arial", 14), 
    bg="#F0F0F0", 
    fg="#333333", 
    pady=10
)
instructions.grid(row=0, column=0, columnspan=9, pady=10)

entries = []
for row in range(9):
    row_entries = []
    for col in range(9):
        entry = tk.Entry(root, width=3, font=("Arial", 18), justify="center", bd=2, relief="ridge")
        entry.grid(row=row+1, column=col, padx=5, pady=5)  # Adjusted row index by +1
        entry.config(fg="green")  # Set user input color to green
        row_entries.append(entry)
    entries.append(row_entries)

# Buttons to solve and clear the Sudoku board
solve_button = tk.Button(root, text="Solve", command=solve, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
solve_button.grid(row=10, column=3, columnspan=3, pady=20)

clear_button = tk.Button(root, text="Clear", command=clear_board, font=("Arial", 14), bg="#F44336", fg="white", padx=10, pady=5)
clear_button.grid(row=11, column=3, columnspan=3, pady=5)

# Start the Tkinter event loop
root.mainloop()
