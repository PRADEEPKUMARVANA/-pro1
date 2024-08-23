import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        
        if height <= 0 or weight <= 0:
            raise ValueError("Height and Weight must be positive values.")
        
        bmi = weight / (height * height)
        label_result['text'] = f"BMI: {bmi:.2f}"
        
        if bmi < 18.5:
            messagebox.showinfo("BMI Result", "You are underweight.")
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo("BMI Result", "You have a normal weight.")
        elif 25 <= bmi < 29.9:
            messagebox.showinfo("BMI Result", "You are overweight.")
        else:
            messagebox.showinfo("BMI Result", "You are obese.")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the height label and entry
label_height = tk.Label(root, text="Height (m):")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Create and place the weight label and entry
label_weight = tk.Label(root, text="Weight (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=10)

# Create and place the result label
label_result = tk.Label(root, text="BMI: ")
label_result.pack(pady=10)

# Run the main event loop
root.mainloop()
