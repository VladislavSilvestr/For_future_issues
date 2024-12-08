from collections import Counter

class TextAnalyzer:
    @staticmethod
    def word_frequency(text):
        words = text.split()
        return dict(Counter(words))