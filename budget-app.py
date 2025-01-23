import tkinter as tk
from tkinter import messagebox, simpledialog

class Budget:
    def __init__(self):
        # Initialize an empty budget dictionary
        self.budget = {}

    def add_category(self, category):
        """Add a new category to the budget."""
        if category not in self.budget:
            self.budget[category] = 0  # Set initial expense to 0
            return f"Category '{category}' added."
        return f"Category '{category}' already exists."

    def add_expense(self, category, amount):
        """Add an expense amount to an existing category."""
        if category in self.budget:
            self.budget[category] += amount  # Add the expense to the category
            return f"Added expense of {amount} to category '{category}'."
        return f"Category '{category}' does not exist. Please add it first."

    def clear_category_expense(self, category):
        """Clear the expenses of a specific category."""
        if category in self.budget:
            self.budget[category] = 0  # Reset category expenses to 0
            return f"Cleared expenses for category '{category}'."
        return f"Category '{category}' does not exist."

    def get_total_expense(self):
        """Get the total of all expenses across categories."""
        return sum(self.budget.values())

    def get_category_expense(self, category):
        """Get the total expense for a specific category."""
        return self.budget.get(category, 0)

class BudgetTrackerApp:
    def __init__(self, master):
        self.master = master
        self.budget = Budget()  # Create a Budget instance

        master.title("Budget Tracker")  # Set the title of the window
        master.geometry("350x300")  # Set the window size

        # Category Listbox Label
        self.category_label = tk.Label(master, text="Categories")
        self.category_label.pack(pady=5)

        # Listbox to display categories and their respective expenses
        self.category_listbox = tk.Listbox(master, width=50)
        self.category_listbox.pack(pady=10)

        # Frame to hold action buttons
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

        # Total Expense Label
        self.total_label = tk.Label(master, text="Total Expenses: $0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

    def add_category(self):
        """Prompt user to add a new category."""
        category = simpledialog.askstring("Add Category", "Enter category name:")
        if category:
            result = self.budget.add_category(category)
            messagebox.showinfo("Add Category", result)  # Show result message
            self.update_category_list()  # Update the displayed list of categories

    def add_expense(self):
        """Prompt user to add an expense to a category."""
        if not self.budget.budget:
            messagebox.showwarning("Warning", "Add a category first!")  # Warning if no categories exist
            return

        category = simpledialog.askstring("Add Expense", "Select category:")
        if category and category in self.budget.budget:
            try:
                amount = simpledialog.askfloat("Add Expense", f"Enter expense amount for {category}:")
                if amount is not None:
                    result = self.budget.add_expense(category, amount)
                    messagebox.showinfo("Add Expense", result)  # Show result message
                    self.update_category_list()  # Update the displayed list of categories
                    self.update_total_expense()  # Update total expenses label
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered")  # Error if amount is invalid
        else:
            messagebox.showerror("Error", "Invalid category")  # Error if category is invalid

    def clear_expense(self):
        """Prompt user to clear expenses for a category."""
        if not self.budget.budget:
            messagebox.showwarning("Warning", "No categories to clear!")  # Warning if no categories exist
            return

        category = simpledialog.askstring("Clear Expense", "Select category to clear:")
        if category and category in self.budget.budget:
            result = self.budget.clear_category_expense(category)
            messagebox.showinfo("Clear Expense", result)  # Show result message
            self.update_category_list()  # Update the displayed list of categories
            self.update_total_expense()  # Update total expenses label
        else:
            messagebox.showerror("Error", "Invalid category")  # Error if category is invalid

    def update_category_list(self):
        """Update the listbox displaying all categories and their expenses."""
        self.category_listbox.delete(0, tk.END)  # Clear the listbox
        for category, amount in self.budget.budget.items():
            # Insert each category and its current expense into the listbox
            self.category_listbox.insert(tk.END, f"{category}: ${amount}")

    def update_total_expense(self):
        """Update the label showing total expenses."""
        total = self.budget.get_total_expense()  # Get the total expenses
        self.total_label.config(text=f"Total Expenses: ${total}")  # Update the total expense label

def main():
    """Initialize the main Tkinter window and run the budget tracker app."""
    root = tk.Tk()  # Create the main window
    app = BudgetTrackerApp(root)  # Create the BudgetTrackerApp instance
    root.mainloop()  # Run the Tkinter event loop

# Entry point of the program, calls the main function when the script is executed
if __name__ == "__main__":
    main()
