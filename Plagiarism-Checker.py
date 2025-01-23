import tkinter as tk
from tkinter import filedialog, messagebox
import difflib

class PlagiarismChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Checker")
        
        self.label1 = tk.Label(root, text="File 1:")
        self.label1.pack()
        
        self.file1_entry = tk.Entry(root, width=50)
        self.file1_entry.pack()
        
        self.browse1_button = tk.Button(root, text="Browse", command=self.browse_file1)
        self.browse1_button.pack()
        
        self.label2 = tk.Label(root, text="File 2:")
        self.label2.pack()
        
        self.file2_entry = tk.Entry(root, width=50)
        self.file2_entry.pack()
        
        self.browse2_button = tk.Button(root, text="Browse", command=self.browse_file2)
        self.browse2_button.pack()
        
        self.check_button = tk.Button(root, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    
    def browse_file1(self):
        file1_path = filedialog.askopenfilename()
        self.file1_entry.insert(0, file1_path)
    
    def browse_file2(self):
        file2_path = filedialog.askopenfilename()
        self.file2_entry.insert(0, file2_path)
    
    def check_plagiarism(self):
        file1_path = self.file1_entry.get()
        file2_path = self.file2_entry.get()
        
        if not file1_path or not file2_path:
            messagebox.showerror("Error", "Please select both files")
            return
        
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_text = file1.read()
            file2_text = file2.read()
        
        similarity = difflib.SequenceMatcher(None, file1_text, file2_text).ratio()
        similarity_percentage = similarity * 100
        
        self.result_label.config(text=f"Similarity: {similarity_percentage:.2f}%")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismChecker(root)
    root.mainloop()