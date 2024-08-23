import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        entry.delete(0, tk.END)

# Function to add a character to the entry widget
def add_to_entry(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button configuration
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=evaluate_expression).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda char=button: add_to_entry(char)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear_entry).grid(row=row_val, column=col_val)

# Run the application
root.mainloop()
