import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
""")
conn.commit()

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration and Login")
        self.master.geometry("300x250")
        self.create_widgets()

    def create_widgets(self):
        # Frame switcher
        self.login_frame = tk.Frame(self.master)
        self.register_frame = tk.Frame(self.master)
        self.login_frame.pack()

        # Login Widgets
        tk.Label(self.login_frame, text="Login", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.login_frame, text="Username").pack()
        self.login_username = tk.Entry(self.login_frame)
        self.login_username.pack()
        tk.Label(self.login_frame, text="Password").pack()
        self.login_password = tk.Entry(self.login_frame, show='*')
        self.login_password.pack()
        tk.Button(self.login_frame, text="Login", command=self.login_user).pack(pady=5)
        tk.Button(self.login_frame, text="Go to Register", command=self.show_register).pack()

        # Register Widgets
        tk.Label(self.register_frame, text="Register", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.register_frame, text="Username").pack()
        self.register_username = tk.Entry(self.register_frame)
        self.register_username.pack()
        tk.Label(self.register_frame, text="Password").pack()
        self.register_password = tk.Entry(self.register_frame, show='*')
        self.register_password.pack()
        tk.Button(self.register_frame, text="Register", command=self.register_user).pack(pady=5)
        tk.Button(self.register_frame, text="Go to Login", command=self.show_login).pack()

    def show_register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack()

    def show_login(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()

    def register_user(self):
        username = self.register_username.get().strip()
        password = self.register_password.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")

    def login_user(self):
        username = self.login_username.get().strip()
        password = self.login_password.get().strip()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Failed", "Invalid username or password.")
            
root = tk.Tk()
app = LoginApp(root)
root.mainloop()
