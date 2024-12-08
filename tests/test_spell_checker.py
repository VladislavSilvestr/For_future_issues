import unittest
from spell_checker.spell_checker import SpellCheck

class TestSpellCheck(unittest.TestCase):
    def setUp(self):
        self.spell_check = SpellCheck()

    def test_check(self):
        result = self.spell_check.check("This is a smaple text with erors.")
        self.assertIn("smaple", result)
        self.assertIn("erors", result)

if __name__ == '__main__':
    unittest.main()