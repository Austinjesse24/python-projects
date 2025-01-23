import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    """
    A simple GUI-based currency converter application.
    """
    def __init__(self, root):
        """
        Initialize the CurrencyConverter application.

        :param root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x200")

        # Currency exchange rates
        self.currencies = {'USD': 1.0, 'EUR': 0.96, 'JPY': 110.0, 'GBP': 0.75}

        # Input for amount
        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)

        # Dropdown for source currency
        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.grid(column=0, row=1, padx=10, pady=10)

        self.from_currency = ttk.Combobox(root, values=list(self.currencies.keys()))
        self.from_currency.grid(column=1, row=1, padx=10, pady=10)
        self.from_currency.current(0)

        # Dropdown for target currency
        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.grid(column=0, row=2, padx=10, pady=10)

        self.to_currency = ttk.Combobox(root, values=list(self.currencies.keys()))
        self.to_currency.grid(column=1, row=2, padx=10, pady=10)
        self.to_currency.current(1)

        # Convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        # Labels to display the result
        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.grid(column=0, row=4, padx=10, pady=10)

        self.result = ttk.Label(root, text="")
        self.result.grid(column=1, row=4, padx=10, pady=10)

    def convert(self):
        """
        Perform the currency conversion based on user input and update the result label.
        """
        try:
            # Get user input for amount and currencies
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            # Perform the conversion
            converted_amount = amount * self.currencies[to_currency] / self.currencies[from_currency]

            # Display the converted amount
            self.result.config(text=f"{converted_amount:.2f} {to_currency}")
        except ValueError:
            # Handle invalid input for amount
            self.result.config(text="Invalid input")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
