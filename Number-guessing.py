import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Number Guessing Game")  # Set the window title
        self.root.geometry("300x150")  # Set the window size

        # Generate a random target number between 1 and 100
        self.target_number = random.randint(1, 100)
        self.attempts = 0  # Track the number of attempts

        # Instruction label
        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)  # Add padding for better layout

        # Entry field for user input
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)  # Add padding below the entry field

        # Button to submit the guess
        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=10)  # Add padding below the button

        # Label to display feedback or results
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)  # Add padding below the result label

    def check_guess(self):
        # Handle the guess entered by the user
        try:
            guess = int(self.entry.get())  # Convert the input to an integer
            self.attempts += 1  # Increment the attempt count

            if guess < self.target_number:
                # If the guess is too low
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                # If the guess is too high
                self.result_label.config(text="Too high! Try again.")
            else:
                # If the guess is correct
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()  # Reset the game for a new round
        except ValueError:
            # Handle non-integer inputs
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        # Reset the game state for a new round
        self.target_number = random.randint(1, 100)  # Generate a new target number
        self.attempts = 0  # Reset the attempt count
        self.entry.delete(0, tk.END)  # Clear the entry field
        self.result_label.config(text="")  # Clear the result label

if __name__ == "__main__":
    # Main function to run the application
    root = tk.Tk()  # Create the main application window
    game = NumberGuessingGame(root)  # Create an instance of the game
    root.mainloop()  # Start the Tkinter event loop
