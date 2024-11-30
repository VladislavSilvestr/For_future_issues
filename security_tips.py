import tkinter as tk
from tkinter import messagebox

def show_security_tips():
    tips = (
        "Safety Tips:\n"
        "1. Use passwords that are at least 12 characters long.\n"
        "2. Combine lowercase and uppercase letters, numbers and special characters.\n"
        "3. Do not use personal information such as names and dates.\n"
        "4. Avoid common words and phrases.\n"
        "5. Change passwords regularly and use different passwords for different accounts."
    )
    messagebox.showinfo("Safety Tips", tips)
