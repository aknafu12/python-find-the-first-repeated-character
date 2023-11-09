import unittest
from first_repeated_char import first_recurring

class TestFindFirstDuplicate(unittest.TestCase):
    def test_first_duplicate(self):
        self.assertEqual("a", first_recurring("kahsay"))
        self.assertEqual(None, first_recurring("tigray"))
        self.assertEqual("i", first_recurring("ethiopia"))
        self.assertNotEqual("e",first_recurring("ethiopia"))
        self.assertIsNone(first_recurring("abcdef"))

        self.assertIsNot("a", first_recurring("abcdef"))

if __name__ == '__main__':
    unittest.main()

