import tkinter as tk

class Calculator:
    def __init__(self, master):
        # Initialize the window (master) and set its title and size
        self.master = master
        master.title("Calculator")
        master.geometry("255x285")

        # Entry field where the input/output is displayed
        self.entry = tk.Entry(master, width=20, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons layout: define button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create the calculator buttons dynamically
        row = 1
        col = 0
        for button in buttons:
            # For each button, define a lambda function to call the `click` method when pressed
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=5, height=2).grid(row=row, column=col, padx=3, pady=3)
            col += 1
            if col > 3:
                col = 0  # Move to the next row after 4 columns
                row += 1

        # Clear button to reset the entry field
        tk.Button(master, text='C', command=self.clear, width=5, height=2).grid(row=row, column=col, padx=3, pady=3)

    def click(self, key):
        """Handle button click events."""
        if key == '=':
            try:
                # Try evaluating the expression in the entry field
                result = eval(self.entry.get())  # This evaluates the entered expression
                self.entry.delete(0, tk.END)  # Clear the entry field
                self.entry.insert(0, result)  # Insert the result into the entry field
            except:
                # If there is an error (like invalid input), display "Error"
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            # For all other buttons (numbers/operators), append the clicked button's text to the entry field
            self.entry.insert(tk.END, key)

    def clear(self):
        """Clear the entry field."""
        self.entry.delete(0, tk.END)

def main():
    """Initialize the main Tkinter window and run the calculator."""
    root = tk.Tk()  # Create the root window
    calc = Calculator(root)  # Initialize the Calculator class
    root.mainloop()  # Run the main loop to keep the window open

# Entry point of the program, calls the main function when the script is executed
if __name__ == "__main__":
    main()
