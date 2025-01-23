import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.category}: ${self.amount:.2f} - {self.description}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        if not category or amount <= 0:
            return "Invalid expense. Category required and amount must be positive."
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        return "Expense added successfully!"

    def view_expenses(self):
        return self.expenses

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

class ExpenseTrackerApp:
    def __init__(self, master):
        self.master = master
        self.tracker = ExpenseTracker()
        
        master.title("Expense Tracker")
        master.geometry("500x600")

        # Expenses Listbox
        self.expenses_label = tk.Label(master, text="Expenses")
        self.expenses_label.pack(pady=5)
        
        self.expenses_listbox = tk.Listbox(master, width=60, height=15)
        self.expenses_listbox.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Add Expense Button
        add_expense_btn = tk.Button(button_frame, text="Add Expense", command=self.add_expense)
        add_expense_btn.pack(side=tk.LEFT, padx=5)

        # View Expenses Button
        view_expenses_btn = tk.Button(button_frame, text="View Expenses", command=self.view_expenses)
        view_expenses_btn.pack(side=tk.LEFT, padx=5)

        # Total Expenses
        self.total_label = tk.Label(master, text="Total Expenses: $0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

    def add_expense(self):
        try:
            amount = simpledialog.askfloat("Add Expense", "Enter amount:")
            if amount is not None and amount > 0:
                category = simpledialog.askstring("Add Expense", "Enter category:")
                if category and category.strip():
                    description = simpledialog.askstring("Add Expense", "Enter description (optional):", initialvalue="")
                    description = description if description else ""
                    
                    result = self.tracker.add_expense(amount, category, description)
                    messagebox.showinfo("Add Expense", result)
                    self.update_expenses_list()
                    self.update_total_expenses()
                else:
                    messagebox.showerror("Error", "Category cannot be empty")
            else:
                messagebox.showerror("Error", "Amount must be a positive number")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_expenses(self):
        expenses = self.tracker.view_expenses()
        if not expenses:
            messagebox.showinfo("Expenses", "No expenses recorded.")
        else:
            # Clear existing list
            self.expenses_listbox.delete(0, tk.END)
            # Populate list with expenses
            for expense in expenses:
                self.expenses_listbox.insert(tk.END, str(expense))

    def update_expenses_list(self):
        self.view_expenses()

    def update_total_expenses(self):
        total = self.tracker.total_expenses()
        self.total_label.config(text=f"Total Expenses: ${total:.2f}")

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()