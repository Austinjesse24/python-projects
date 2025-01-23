from tkinter import Tk, Label, Listbox, Button, Frame, simpledialog, messagebox
import datetime

class Expense:
    def __init__(self, amount, category, description=""):
        # Initialize an expense with amount, category, description, and current date
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()

    def __str__(self):
        # String representation of the expense
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.category}: ${self.amount:.2f} - {self.description}"

class ExpenseTracker:
    def __init__(self):
        # Initialize an empty list to store expenses
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        # Add a new expense after validation
        if not category or amount <= 0:
            return "Invalid expense. Category required and amount must be positive."
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        return "Expense added successfully!"

    def view_expenses(self):
        # Return the list of all expenses
        return self.expenses

    def total_expenses(self):
        # Calculate and return the total amount of expenses
        return sum(expense.amount for expense in self.expenses)

class ExpenseTrackerApp:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        self.tracker = ExpenseTracker()  # Create an instance of ExpenseTracker
        
        master.title("Expense Tracker")  # Set the window title
        master.geometry("500x600")  # Set the window size

        # Label for displaying "Expenses"
        self.expenses_label = Label(master, text="Expenses")
        self.expenses_label.pack(pady=5)
        
        # Listbox to display the list of expenses
        self.expenses_listbox = Listbox(master, width=60, height=15)
        self.expenses_listbox.pack(pady=10)

        # Frame to hold buttons
        button_frame = Frame(master)
        button_frame.pack(pady=10)

        # Button to add a new expense
        add_expense_btn = Button(button_frame, text="Add Expense", command=self.add_expense)
        add_expense_btn.pack(side="left", padx=5)

        # Button to view all expenses
        view_expenses_btn = Button(button_frame, text="View Expenses", command=self.view_expenses)
        view_expenses_btn.pack(side="left", padx=5)

        # Label to display the total expenses
        self.total_label = Label(master, text="Total Expenses: $0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

    def add_expense(self):
        # Add a new expense using dialog boxes for input
        try:
            # Prompt for amount
            amount = simpledialog.askfloat("Add Expense", "Enter amount:")
            if amount is None or amount <= 0:
                messagebox.showerror("Error", "Amount must be a positive number")
                return
            
            # Prompt for category
            category = simpledialog.askstring("Add Expense", "Enter category:")
            if not category or not category.strip():
                messagebox.showerror("Error", "Category cannot be empty")
                return
            
            # Prompt for description (optional)
            description = simpledialog.askstring("Add Expense", "Enter description (optional):")
            description = description if description else ""
            
            # Add the expense to the tracker
            result = self.tracker.add_expense(amount, category, description)
            messagebox.showinfo("Add Expense", result)
            
            # Update the UI
            self.update_expenses_list()
            self.update_total_expenses()
        except Exception as e:
            # Handle any unexpected errors
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_expenses(self):
        # View all expenses in the listbox
        self.expenses_listbox.delete(0, "end")  # Clear the Listbox
        expenses = self.tracker.view_expenses()  # Fetch all expenses
        if not expenses:
            self.expenses_listbox.insert("end", "No expenses recorded.")
        else:
            for expense in expenses:
                self.expenses_listbox.insert("end", str(expense))

    def update_expenses_list(self):
        # Refresh the expenses displayed in the Listbox
        self.view_expenses()

    def update_total_expenses(self):
        # Update the total expenses label
        total = self.tracker.total_expenses()
        self.total_label.config(text=f"Total Expenses: ${total:.2f}")

# Main function to run the application
def main():
    root = Tk()  # Create the main application window
    app = ExpenseTrackerApp(root)  # Create an instance of the ExpenseTrackerApp
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()
