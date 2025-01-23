import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove!")

def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x450")

# Create and place widgets
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=remove_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

clear_button = tk.Button(root, text="Clear All Tasks", width=15, command=clear_tasks)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
