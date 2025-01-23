import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        # Initialize the game window and setup
        self.root = root
        self.root.title("Tic Tac Toe")  # Set the title of the game window
        self.player = 'X'  # Initial player is 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # 3x3 grid of buttons
        self.create_buttons()  # Create the buttons for the grid

    def create_buttons(self):
        # Create a 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root,
                    text='',  # Initial button text is empty
                    font=('normal', 40),  # Set font style and size
                    width=5, height=2,  # Button dimensions
                    command=lambda i=i, j=j: self.on_button_click(i, j)  # Handle button click
                )
                self.buttons[i][j].grid(row=i, column=j)  # Place the button in the grid

    def on_button_click(self, i, j):
        # Handle button click event
        if self.buttons[i][j]['text'] == '' and not self.check_winner():
            # If the button is empty and there is no winner yet
            self.buttons[i][j]['text'] = self.player  # Set button text to current player
            if self.check_winner():
                # Check if the current move results in a win
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_board()  # Reset the board for a new game
            elif self.check_draw():
                # Check if the game ends in a draw
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()  # Reset the board for a new game
            else:
                # Switch to the other player
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        # Check all winning conditions (rows, columns, diagonals)
        for i in range(3):
            # Check rows
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                return True
            # Check columns
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                return True
        # Check diagonals
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        return False

    def check_draw(self):
        # Check if all buttons are filled and there is no winner
        for row in self.buttons:
            for button in row:
                if button['text'] == '':  # If any button is still empty, it's not a draw
                    return False
        return True

    def reset_board(self):
        # Reset the board for a new game
        for row in self.buttons:
            for button in row:
                button['text'] = ''  # Clear all button texts
        self.player = 'X'  # Reset the starting player to 'X'

if __name__ == "__main__":
    # Main function to start the game
    root = tk.Tk()  # Create the main application window
    game = TicTacToe(root)  # Create the Tic Tac Toe game instance
    root.mainloop()  # Start the Tkinter event loop
