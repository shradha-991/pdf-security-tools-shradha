import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path.set(filepath)

def browse_wordlist():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    wordlist_path.set(filepath)

def crack_pdf():
    pdf_file = pdf_path.get()
    wordlist_file = wordlist_path.get()

    if not pdf_file or not wordlist_file:
        messagebox.showwarning("Input Required", "Please select both PDF and Wordlist files.")
        return

    try:
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            with open(wordlist_file, "r") as words:
                for line in words:
                    password = line.strip()
                    try:
                        if reader.decrypt(password):
                            messagebox.showinfo("Success", f"Password found: {password}")
                            return
                    except:
                        pass
        messagebox.showerror("Failed", "Password not found in wordlist.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setup for gui
root = tk.Tk()
root.title("PDF Cracker Tool")
root.geometry("400x300")

pdf_path = tk.StringVar()
wordlist_path = tk.StringVar()

tk.Label(root, text="PDF File:").pack(pady=5)
tk.Entry(root, textvariable=pdf_path, width=50).pack()
tk.Button(root, text="Browse PDF", command=browse_pdf).pack(pady=5)

tk.Label(root, text="Wordlist File:").pack(pady=5)
tk.Entry(root, textvariable=wordlist_path, width=50).pack()
tk.Button(root, text="Browse Wordlist", command=browse_wordlist).pack(pady=5)

tk.Button(root, text="Crack PDF", command=crack_pdf, bg="#007acc", fg="white", padx=10, pady=5).pack(pady=20)

root.mainloop()
