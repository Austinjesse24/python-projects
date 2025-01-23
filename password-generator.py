# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password

# if __name__ == "__main__":
#     print("Generated Password:", generate_password())

import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x300")

        # Length Selection
        tk.Label(master, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        self.length_slider = tk.Scale(master, from_=4, to=32, 
                                       orient=tk.HORIZONTAL, 
                                       variable=self.length_var)
        self.length_slider.pack(pady=5)

        # Character Set Options
        self.use_letters = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_punctuation = tk.BooleanVar(value=True)

        tk.Checkbutton(master, text="Letters", variable=self.use_letters).pack()
        tk.Checkbutton(master, text="Digits", variable=self.use_digits).pack()
        tk.Checkbutton(master, text="Punctuation", variable=self.use_punctuation).pack()

        # Generate Button
        tk.Button(master, text="Generate Password", command=self.generate_password).pack(pady=10)

        # Password Display
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master, textvariable=self.password_var, width=40)
        self.password_entry.pack(pady=10)

        # Copy Button
        tk.Button(master, text="Copy to Clipboard", command=self.copy_password).pack(pady=5)

    def generate_password(self):
        characters = ""
        if self.use_letters.get():
            characters += string.ascii_letters
        if self.use_digits.get():
            characters += string.digits
        if self.use_punctuation.get():
            characters += string.punctuation

        if not characters:
            self.password_var.set("Select at least one character type")
            return

        length = self.length_var.get()
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def copy_password(self):
        password = self.password_var.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(password)

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()