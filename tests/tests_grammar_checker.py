import unittest
from grammar_checker import GrammarCheck

class TestGrammarCheck(unittest.TestCase):
    def setUp(self):
        self.grammar_check = GrammarCheck()

    def test_check(self):
        result = self.grammar_check.check("She go to the market.")
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()