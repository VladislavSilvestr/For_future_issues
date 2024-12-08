from spellchecker import SpellChecker

class SpellCheck:
    def __init__(self):
        self.spell = SpellChecker()
    
    def check(self, text):
        words = text.split()
        misspelled = self.spell.unknown(words)
        return misspelled