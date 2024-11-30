import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
from password_generator import generate_password
from security_tips import show_security_tips

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_passwords():
    try:
        length = int(length_entry.get())
        num_passwords = int(num_passwords_entry.get())
        
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_special_chars = special_chars_var.get()

        passwords = []
        for _ in range(num_passwords):
            password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
            passwords.append(password)

        password_label.config(text="\n".join(passwords))
        
        if messagebox.askyesno("Save passwords?", "Do you want to save the generated passwords?"):
            save_passwords(passwords)
            messagebox.showinfo("Passwords saved", "Passwords successfully saved to file.")
    except ValueError:
        messagebox.showerror("Input error", "Please enter correct values.")

def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Copy", "Password copied to clipboard.")

def save_passwords(passwords):
    with open("generated_passwords.txt", "a") as file:
        for password in passwords:
            file.write(password + "\n")

root = tk.Tk()
root.title("Password generator")

length_label = tk.Label(root, text="Password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

num_passwords_label = tk.Label(root, text="Number of passwords:")
num_passwords_label.pack()
num_passwords_entry = tk.Entry(root)
num_passwords_entry.pack()

complexity_var = tk.StringVar(value="Low")
complexity_label = tk.Label(root, text="Difficulty level:")
complexity_label.pack()
complexity_options = ["Low", "Medium", "High"]
complexity_menu = tk.OptionMenu(root, complexity_var, *complexity_options)
complexity_menu.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Use capital letters", variable=uppercase_var)
uppercase_check.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Use numbers", variable=numbers_var)
numbers_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Use special characters", variable=special_chars_var)
special_chars_check.pack()

base_word_label = tk.Label(root, text="Base word (optional):")
base_word_label.pack()
base_word_entry = tk.Entry(root)
base_word_entry.pack()

generate_button = tk.Button(root, text="Generate password", command=generate_and_display_passwords)
generate_button.pack()

password_label = tk.Label(root, text="", justify=tk.LEFT)
password_label.pack()

tips_button = tk.Button(root, text="Safety Tips", command=show_security_tips)
tips_button.pack()

root.mainloop()
