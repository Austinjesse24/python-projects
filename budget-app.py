class Budget:
    def __init__(self):
        self.budget = {}

    def add_category(self, category):
        if category not in self.budget:
            self.budget[category] = 0
            print(f"Category '{category}' added.")
        else:
            print(f"Category '{category}' already exists.")

    def add_expense(self, category, amount):
        if category in self.budget:
            self.budget[category] += amount
            print(f"Added expense of {amount} to category '{category}'.")
        else:
            print(f"Category '{category}' does not exist. Please add it first.")

    def get_total_expense(self):
        total = sum(self.budget.values())
        print(f"Total expense: {total}")
        return total

    def get_category_expense(self, category):
        if category in self.budget:
            print(f"Total expense for category '{category}': {self.budget[category]}")
            return self.budget[category]
        else:
            print(f"Category '{category}' does not exist.")
            return 0

    def display_budget(self):
        print("Budget Summary:")
        for category, amount in self.budget.items():
            print(f"{category}: {amount}")

if __name__ == "__main__":
    budget_app = Budget()
    while True:
        print("\nBudget Application")
        print("1. Add Category")
        print("2. Add Expense")
        print("3. Get Total Expense")
        print("4. Get Category Expense")
        print("5. Display Budget")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category name: ")
            budget_app.add_category(category)
        elif choice == '2':
            category = input("Enter category name: ")
            amount = float(input("Enter expense amount: "))
            budget_app.add_expense(category, amount)
        elif choice == '3':
            budget_app.get_total_expense()
        elif choice == '4':
            category = input("Enter category name: ")
            budget_app.get_category_expense(category)
        elif choice == '5':
            budget_app.display_budget()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")