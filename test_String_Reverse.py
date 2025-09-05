import unittest
from main import reverse_string

class TestReverseString(unittest.TestCase):

    def test_basic_strings(self):
        """Test simple words"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("abc"), "cba")

    def test_with_spaces(self):
        """Test strings containing spaces"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string(" a b "), " b a ")

    def test_empty_string(self):
        """Test empty string"""
        self.assertEqual(reverse_string(""), "")

    def test_palindromes(self):
        """Test palindromes (same reversed)"""
        self.assertEqual(reverse_string("madam"), "madam")
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_with_numbers_and_symbols(self):
        """Test strings with numbers and special characters"""
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("hello!"), "!olleh")

if __name__ == "__main__":
    unittest.main()

