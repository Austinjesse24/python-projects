# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ['1', '2', '3', '4']:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f"{num1} + {num2} = {add(num1, num2)}")
#         elif choice == '2':
#             print(f"{num1} - {num2} = {subtract(num1, num2)}")
#         elif choice == '3':
#             print(f"{num1} * {num2} = {multiply(num1, num2)}")
#         elif choice == '4':
#             print(f"{num1} / {num2} = {divide(num1, num2)}")
#     else:
#         print("Invalid input")

# if __name__ == "__main__":
#     calculator()


import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")

        # Entry field
        self.entry = tk.Entry(master, width=20, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=5, height=2).grid(row=row, column=col, padx=3, pady=3)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        tk.Button(master, text='C', command=self.clear, width=5, height=2).grid(row=row, column=col, padx=3, pady=3)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, key)

    def clear(self):
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()