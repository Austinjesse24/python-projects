import tkinter as tk
from tkinter import messagebox, simpledialog

class Budget:
    def __init__(self):
        self.budget = {}

    def add_category(self, category):
        if category not in self.budget:
            self.budget[category] = 0
            return f"Category '{category}' added."
        return f"Category '{category}' already exists."

    def add_expense(self, category, amount):
        if category in self.budget:
            self.budget[category] += amount
            return f"Added expense of {amount} to category '{category}'."
        return f"Category '{category}' does not exist. Please add it first."

    def clear_category_expense(self, category):
        if category in self.budget:
            self.budget[category] = 0
            return f"Cleared expenses for category '{category}'."
        return f"Category '{category}' does not exist."

    def get_total_expense(self):
        return sum(self.budget.values())

    def get_category_expense(self, category):
        return self.budget.get(category, 0)

class BudgetTrackerApp:
    def __init__(self, master):
        self.master = master
        self.budget = Budget()
        
        master.title("Budget Tracker")
        master.geometry("400x550")

        # Category Listbox
        self.category_label = tk.Label(master, text="Categories")
        self.category_label.pack(pady=5)
        
        self.category_listbox = tk.Listbox(master, width=50)
        self.category_listbox.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Add Category Button
        add_category_btn = tk.Button(button_frame, text="Add Category", command=self.add_category)
        add_category_btn.pack(side=tk.LEFT, padx=5)

        # Add Expense Button
        add_expense_btn = tk.Button(button_frame, text="Add Expense", command=self.add_expense)
        add_expense_btn.pack(side=tk.LEFT, padx=5)

        # Clear Expense Button
        clear_expense_btn = tk.Button(button_frame, text="Clear Expense", command=self.clear_expense)
        clear_expense_btn.pack(side=tk.LEFT, padx=5)

        # Total Expense
        self.total_label = tk.Label(master, text="Total Expenses: $0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

    def add_category(self):
        category = simpledialog.askstring("Add Category", "Enter category name:")
        if category:
            result = self.budget.add_category(category)
            messagebox.showinfo("Add Category", result)
            self.update_category_list()

    def add_expense(self):
        if not self.budget.budget:
            messagebox.showwarning("Warning", "Add a category first!")
            return

        category = simpledialog.askstring("Add Expense", "Select category:")
        if category and category in self.budget.budget:
            try:
                amount = simpledialog.askfloat("Add Expense", f"Enter expense amount for {category}:")
                if amount is not None:
                    result = self.budget.add_expense(category, amount)
                    messagebox.showinfo("Add Expense", result)
                    self.update_category_list()
                    self.update_total_expense()
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered")
        else:
            messagebox.showerror("Error", "Invalid category")

    def clear_expense(self):
        if not self.budget.budget:
            messagebox.showwarning("Warning", "No categories to clear!")
            return

        category = simpledialog.askstring("Clear Expense", "Select category to clear:")
        if category and category in self.budget.budget:
            result = self.budget.clear_category_expense(category)
            messagebox.showinfo("Clear Expense", result)
            self.update_category_list()
            self.update_total_expense()
        else:
            messagebox.showerror("Error", "Invalid category")

    def update_category_list(self):
        self.category_listbox.delete(0, tk.END)
        for category, amount in self.budget.budget.items():
            self.category_listbox.insert(tk.END, f"{category}: ${amount}")

    def update_total_expense(self):
        total = self.budget.get_total_expense()
        self.total_label.config(text=f"Total Expenses: ${total}")

def main():
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()