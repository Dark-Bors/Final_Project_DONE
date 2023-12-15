# login_page.py
import tkinter as tk
from tkinter import messagebox  # to display the message box
from customtkinter import CTk, CTkEntry, CTkButton
from app_logging import logger  # make sure you have this import if you want to log the message

class LoginPage(CTk):
    def __init__(self, parent, login_callback):
        super().__init__()
        self.parent = parent
        self.login_callback = login_callback

        self.title("Login")
        self.geometry("300x200")

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        
        self.username_entry = CTkEntry(self, width=200)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = CTkEntry(self, width=200, show="*")
        self.password_entry.pack()

        self.login_button = CTkButton(self, text="Login", command=self.on_login_clicked)
        self.login_button.pack()

    def on_login_clicked(self):
        # Here you can add your authentication logic
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Example: Check if the credentials are correct
        if username == "boris" and password == "123":
            self.destroy()  # Close the login window
            self.login_callback()  # Call the callback to open the main application
        else:
            # Display error message
            messagebox.showerror("Login Failed", "Incorrect username or password")
            # Log the failed login attempt
            logger.error(f"Failed login attempt with username: {username}")
