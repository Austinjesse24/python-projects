# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# def main():
#     print("Welcome to the BMI Calculator")
#     weight = float(input("Enter your weight in kilograms: "))
#     height = float(input("Enter your height in meters: "))
    
#     bmi = calculate_bmi(weight, height)
#     print(f"Your BMI is: {bmi:.2f}")
    
#     if bmi < 18.5:
#         print("You are underweight.")
#     elif 18.5 <= bmi < 24.9:
#         print("You have a normal weight.")
#     elif 25 <= bmi < 29.9:
#         print("You are overweight.")
#     else:
#         print("You are obese.")

# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    """Calculate BMI based on weight and height."""
    height = height / 100  # Convert cm to meter
    bmi = weight / (height ** 2)
    return bmi

def show_bmi_result():
    """Process input and display BMI result."""
    try:
        # Retrieve values from entry fields
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        # Show result in a message box
        messagebox.showinfo("BMI Result", 
                             f"Your BMI is: {bmi:.2f}\n"
                             f"Category: {category}")
    
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Error", "Please enter valid numbers for weight and height")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Weight input
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Height input
height_label = tk.Label(root, text="Height (cm):")
height_label.pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=show_bmi_result)
calculate_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()