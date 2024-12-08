import tkinter as tk
from gui.widgets import TextEditor, CheckButton

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("800x600")
        
        self.text_editor = TextEditor(self.master)
        self.result_display = tk.Text(self.master, height=10, state='disabled')
        self.check_button = CheckButton(self.master, self.text_editor, self.result_display)

        self.text_editor.pack(expand=True, fill='both')
        self.check_button.pack(side='bottom')
        self.result_display.pack(side='bottom', fill='x')