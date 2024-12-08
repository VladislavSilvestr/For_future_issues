import tkinter as tk
from spell_checker.spell_checker import SpellCheck
from grammar_checker.grammar_checker import GrammarCheck

class TextEditor(tk.Text):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill='both')

class CheckButton(tk.Button):
    def __init__(self, master, text_editor, result_display):
        super().__init__(master, text="Check Text", command=lambda: self.check_text(text_editor, result_display))
        self.spell_checker = SpellCheck()
        self.grammar_checker = GrammarCheck()

    def check_text(self, text_editor, result_display):
        text = text_editor.get("1.0", tk.END)

        misspelled = self.spell_checker.check(text)
        result_display.config(state='normal')
        result_display.delete("1.0", tk.END)

        if misspelled:
            result_display.insert(tk.END, "Misspelled words:\n" + "\n".join(misspelled) + "\n")
        else:
            result_display.insert(tk.END, "No spelling errors found.\n")

        corrected_text = self.grammar_checker.check(text)
        if corrected_text != text:
            result_display.insert(tk.END, "Corrected text:\n" + corrected_text + "\n")
        else:
            result_display.insert(tk.END, "No grammar errors found.\n")

        result_display.config(state='disabled')

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.light_theme = {
            "bg": "white",
            "fg": "black",
            "highlightbackground": "lightgray",
            "highlightcolor": "gray"
        }

        self.dark_theme = {
            "bg": "#2E2E2E",
            "fg": "white",
            "highlightbackground": "#4A4A4A",
            "highlightcolor": "gray"
        }

        self.current_theme = self.light_theme

        self.text_editor = TextEditor(master)
        self.result_display = TextEditor(master)
        self.result_display.config(state='disabled')

        self.check_button = CheckButton(master, self.text_editor, self.result_display)
        self.check_button.pack()

        self.theme_button = tk.Button(master, text="Switch to Dark Theme", command=self.toggle_theme)
        self.theme_button.pack(side=tk.BOTTOM)

        self.apply_theme()

    def toggle_theme(self):
        if self.current_theme == self.light_theme:
            self.current_theme = self.dark_theme
            self.theme_button.config(text="Switch to Light Theme")
        else:
            self.current_theme = self.light_theme
            self.theme_button.config(text="Switch to Dark Theme")

        self.apply_theme()

    def apply_theme(self):
        self.text_editor.config(bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.result_display.config(bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.text_editor.tag_configure("highlight", background=self.current_theme["highlightbackground"], foreground=self.current_theme["fg"])
        self.text_editor.focus()

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()