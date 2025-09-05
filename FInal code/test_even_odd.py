import unittest
from main import check_odd_even

class TestOddEven(unittest.TestCase):

    def test_even_numbers(self):
        """Test even numbers"""
        self.assertEqual(check_odd_even(2), "2 is Even")
        self.assertEqual(check_odd_even(0), "0 is Even")
        self.assertEqual(check_odd_even(100), "100 is Even")

    def test_odd_numbers(self):
        """Test odd numbers"""
        self.assertEqual(check_odd_even(1), "1 is Odd")
        self.assertEqual(check_odd_even(7), "7 is Odd")
        self.assertEqual(check_odd_even(99), "99 is Odd")

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(check_odd_even(-2), "-2 is Even")
        self.assertEqual(check_odd_even(-7), "-7 is Odd")

if __name__ == "__main__":
    unittest.main()

