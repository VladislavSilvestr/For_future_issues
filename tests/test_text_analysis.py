import unittest
from text_analysis.analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def test_word_frequency(self):
        result = TextAnalyzer.word_frequency("hello world hello")
        self.assertEqual(result["hello"], 2)
        self.assertEqual(result["world"], 1)

if __name__ == '__main__':
    unittest.main()