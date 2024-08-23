import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        result_text.set(f"Your BMI is {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk()
root.title("Superhero BMI Calculator")

# Set window size
root.geometry("400x300")

# Set superhero background
background_image = tk.PhotoImage(file="superhero_background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame to hold the widgets
frame = tk.Frame(root, bg="lightblue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.5, anchor="n")

# Create weight and height labels and entries
label_weight = tk.Label(frame, text="Weight (kg):", font=("Comic Sans MS", 12), bg="lightblue")
label_weight.place(relx=0.1, rely=0.2, relwidth=0.35, relheight=0.2)

entry_weight = tk.Entry(frame, font=("Comic Sans MS", 12))
entry_weight.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.2)

label_height = tk.Label(frame, text="Height (m):", font=("Comic Sans MS", 12), bg="lightblue")
label_height.place(relx=0.1, rely=0.5, relwidth=0.35, relheight=0.2)

entry_height = tk.Entry(frame, font=("Comic Sans MS", 12))
entry_height.place(relx=0.5, rely=0.5, relwidth=0.35, relheight=0.2)

# Create a result label
result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text, font=("Comic Sans MS", 14), bg="yellow")
label_result.place(relx=0.5, rely=0.7, anchor="n")

# Create a calculate button
button_calculate = tk.Button(root, text="Calculate BMI", font=("Comic Sans MS", 12), command=calculate_bmi)
button_calculate.place(relx=0.5, rely=0.85, anchor="n")

# Run the application
root.mainloop()
