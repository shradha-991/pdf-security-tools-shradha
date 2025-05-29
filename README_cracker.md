# 🔓 PDF Cracker Tool using Python (GUI Based)

This is a GUI-based Python tool developed to simulate a dictionary attack on password-protected PDF files. It allows users to select a locked PDF and a wordlist, and attempts to crack the file using all passwords listed.

---

## 🔧 Technologies Used

- Python 3.11  
- tkinter  
- PyPDF2  
- OS module

---

## 💡 Features

- GUI-based interface (no command line required)  
- Browse & select PDF and wordlist files  
- Attempts to decrypt the PDF using each password in the wordlist  
- Shows success message with the correct password (if found)  
- Displays failure message if the password is not in the wordlist  
- Saves the cracked/unlocked PDF (if successful)

---

## 📷 Screenshots

📁 Please refer to the `SCREENSHOTSS/` folder for:
- GUI Interface  
- Success Message (Password Found)  
- Failure Message (Password Not Found)

---

## 📄 Project Report & Code

- 🔹 Report: 'PROJECT_REPORT_PDF_Cracker_Shradha.pptx'
- 🔹 Code File: `cracker_gui.py`  
- 🔹 Sample wordlist: `wordlist.txt`  
- 🔹 Sample locked file: `locked.pdf`  
- 🔹 Output file (if cracked): `unlocked.pdf`

---

##
- This tool is created for educational and ethical demonstration purposes only.  
- Cracking depends on whether the correct password exists in the selected wordlist.  
- If the password is missing from the wordlist, the tool will not be able to unlock the file.


