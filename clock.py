import tkinter as tk
import time

def time_update():
    """
    Update the clock label with the current time every second.
    """
    # Get the current time in the desired format
    current_time = time.strftime('%H:%M:%S %p')
    
    # Update the text of the clock label
    clock_label.config(text=current_time)
    
    # Schedule the function to run again after 1000 milliseconds (1 second)
    clock_label.after(1000, time_update)

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")  # Set the title of the window

# Create a label to display the clock
clock_label = tk.Label(
    root,
    font=('calibri', 30, 'bold'),  # Set font type, size, and style
    background='blue',            # Set the background color
    foreground='white'            # Set the text color
)
clock_label.pack(anchor='center')  # Center the label in the window

# Start updating the clock
time_update()

# Run the Tkinter event loop
root.mainloop()
