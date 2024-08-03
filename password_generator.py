import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.length_var = tk.IntVar(value=12)
        self.include_letters_var = tk.BooleanVar(value=True)
        self.include_numbers_var = tk.BooleanVar(value=True)
        self.include_symbols_var = tk.BooleanVar(value=True)
        self.exclude_chars_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:", bg="#f0f0f0", fg="#333333").pack(pady=5)
        tk.Entry(self.root, textvariable=self.length_var, bg="#ffffff", fg="#333333").pack(pady=5)

        tk.Checkbutton(self.root, text="Include Letters", variable=self.include_letters_var, bg="#f0f0f0", fg="#333333").pack(pady=5)
        tk.Checkbutton(self.root, text="Include Numbers", variable=self.include_numbers_var, bg="#f0f0f0", fg="#333333").pack(pady=5)
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols_var, bg="#f0f0f0", fg="#333333").pack(pady=5)

        tk.Label(self.root, text="Exclude Characters:", bg="#f0f0f0", fg="#333333").pack(pady=5)
        tk.Entry(self.root, textvariable=self.exclude_chars_var, bg="#ffffff", fg="#333333").pack(pady=5)

        tk.Button(self.root, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="#ffffff").pack(pady=10)
        self.password_entry = tk.Entry(self.root, width=30, bg="#ffffff", fg="#333333")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#2196F3", fg="#ffffff").pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        include_letters = self.include_letters_var.get()
        include_numbers = self.include_numbers_var.get()
        include_symbols = self.include_symbols_var.get()
        exclude_chars = self.exclude_chars_var.get()

        character_set = ''
        if include_letters:
            character_set += string.ascii_letters
        if include_numbers:
            character_set += string.digits
        if include_symbols:
            character_set += string.punctuation
        
        if exclude_chars:
            character_set = ''.join(ch for ch in character_set if ch not in exclude_chars)

        if not character_set:
            messagebox.showerror("Error", "No characters available for password generation")
            return

        password = ''.join(random.choice(character_set) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard")
        else:
            messagebox.showwarning("Warning", "No password to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
