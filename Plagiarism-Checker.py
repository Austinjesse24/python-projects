import tkinter as tk
from tkinter import filedialog, messagebox
import difflib

class PlagiarismChecker:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Plagiarism Checker")  # Set the title of the window

        # Label and entry field for the first file
        self.label1 = tk.Label(root, text="File 1:")
        self.label1.pack()
        
        self.file1_entry = tk.Entry(root, width=50)  # Input field for File 1
        self.file1_entry.pack()
        
        self.browse1_button = tk.Button(root, text="Browse", command=self.browse_file1)
        self.browse1_button.pack()  # Button to browse File 1

        # Label and entry field for the second file
        self.label2 = tk.Label(root, text="File 2:")
        self.label2.pack()
        
        self.file2_entry = tk.Entry(root, width=50)  # Input field for File 2
        self.file2_entry.pack()
        
        self.browse2_button = tk.Button(root, text="Browse", command=self.browse_file2)
        self.browse2_button.pack()  # Button to browse File 2

        # Button to check for plagiarism
        self.check_button = tk.Button(root, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.pack()

        # Label to display the result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    
    def browse_file1(self):
        # Open a file dialog to select File 1
        file1_path = filedialog.askopenfilename()
        self.file1_entry.insert(0, file1_path)  # Display selected file path in the entry field
    
    def browse_file2(self):
        # Open a file dialog to select File 2
        file2_path = filedialog.askopenfilename()
        self.file2_entry.insert(0, file2_path)  # Display selected file path in the entry field
    
    def check_plagiarism(self):
        # Get file paths from the entry fields
        file1_path = self.file1_entry.get()
        file2_path = self.file2_entry.get()

        # Ensure both files are selected
        if not file1_path or not file2_path:
            messagebox.showerror("Error", "Please select both files")  # Show error if any file is missing
            return

        # Read the content of both files
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_text = file1.read()
            file2_text = file2.read()

        # Calculate similarity using difflib
        similarity = difflib.SequenceMatcher(None, file1_text, file2_text).ratio()
        similarity_percentage = similarity * 100  # Convert ratio to percentage

        # Display the similarity percentage
        self.result_label.config(text=f"Similarity: {similarity_percentage:.2f}%")
        
if __name__ == "__main__":
    # Main function to run the application
    root = tk.Tk()  # Create the main application window
    app = PlagiarismChecker(root)  # Create an instance of PlagiarismChecker
    root.mainloop()  # Start the Tkinter event loop
