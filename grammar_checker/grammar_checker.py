from textblob import TextBlob

class GrammarCheck:
    def __init__(self):
        pass
    
    def check(self, text):
        blob = TextBlob(text)
        corrected_text = str(blob.correct())
        return corrected_text