import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

def protect_pdf(input_file, output_file, password):
    try:
        with open(input_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            with open(output_file, 'wb') as protected_file:
                writer.write(protected_file)

        messagebox.showinfo("Success", f"PDF protected and saved as:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def start_protection():
    input_path = entry_input.get()
    password = entry_password.get()

    if not input_path or not password:
        messagebox.showwarning("Missing Info", "Please select a file and enter a password.")
        return

    output_path = os.path.splitext(input_path)[0] + "_protected.pdf"
    protect_pdf(input_path, output_path, password)



# GUI Setup
root = tk.Tk()
root.title("PDF Protection Tool")
root.geometry("400x200")

label_input = tk.Label(root, text="Select PDF File:")
label_input.pack(pady=(10, 0))

entry_input = tk.Entry(root, width=40)
entry_input.pack(pady=5)

btn_browse = tk.Button(root, text="Browse", command=browse_file)
btn_browse.pack()

label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=(10, 0))

entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

btn_protect = tk.Button(root, text="Protect PDF", command=start_protection)
btn_protect.pack(pady=10)

root.mainloop()
