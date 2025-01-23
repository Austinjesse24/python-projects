import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        master.title("Password Generator")  # Set the title of the window
        master.geometry("400x300")  # Set the window size

        # Password length selection
        tk.Label(master, text="Password Length:").pack(pady=5)  # Label for password length
        self.length_var = tk.IntVar(value=12)  # Default password length
        self.length_slider = tk.Scale(master, 
                                       from_=4, to=32,  # Slider range (min=4, max=32)
                                       orient=tk.HORIZONTAL,  # Horizontal slider
                                       variable=self.length_var)  # Bind slider to variable
        self.length_slider.pack(pady=5)

        # Character set options (letters, digits, punctuation)
        self.use_letters = tk.BooleanVar(value=True)  # Include letters by default
        self.use_digits = tk.BooleanVar(value=True)  # Include digits by default
        self.use_punctuation = tk.BooleanVar(value=True)  # Include punctuation by default

        tk.Checkbutton(master, text="Letters", variable=self.use_letters).pack()  # Checkbox for letters
        tk.Checkbutton(master, text="Digits", variable=self.use_digits).pack()  # Checkbox for digits
        tk.Checkbutton(master, text="Punctuation", variable=self.use_punctuation).pack()  # Checkbox for punctuation

        # Generate button
        tk.Button(master, text="Generate Password", command=self.generate_password).pack(pady=10)  # Button to generate password

        # Password display
        self.password_var = tk.StringVar()  # Variable to hold generated password
        self.password_entry = tk.Entry(master, textvariable=self.password_var, width=40)  # Entry field to display password
        self.password_entry.pack(pady=10)

        # Copy to clipboard button
        tk.Button(master, text="Copy to Clipboard", command=self.copy_password).pack(pady=5)  # Button to copy password

    def generate_password(self):
        # Generate a random password based on selected options
        characters = ""
        if self.use_letters.get():
            characters += string.ascii_letters  # Add letters to character set
        if self.use_digits.get():
            characters += string.digits  # Add digits to character set
        if self.use_punctuation.get():
            characters += string.punctuation  # Add punctuation to character set

        if not characters:
            # Display error if no character set is selected
            self.password_var.set("Select at least one character type")
            return

        length = self.length_var.get()  # Get the desired password length
        password = ''.join(random.choice(characters) for _ in range(length))  # Generate password
        self.password_var.set(password)  # Display the generated password

    def copy_password(self):
        # Copy the generated password to the clipboard
        password = self.password_var.get()  # Get the password from the entry field
        self.master.clipboard_clear()  # Clear the clipboard
        self.master.clipboard_append(password)  # Append the password to the clipboard

def main():
    # Main function to run the application
    root = tk.Tk()  # Create the main application window
    app = PasswordGenerator(root)  # Create an instance of PasswordGenerator
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()
