import unittest
from get_sum_of_even_valued_fibonacci_terms_below_limit import get_sum_of_even_valued_fibonacci_terms_below_limit


class Test_get_sum_of_even_valued_fibonacci_terms_below_limit(unittest.TestCase):

    def test_positive_branch(self):
        self.assertEqual(
            get_sum_of_even_valued_fibonacci_terms_below_limit(100), 44)

    def test_negative_branch(self):
        self.assertNotEqual(
            get_sum_of_even_valued_fibonacci_terms_below_limit(100), 45)

    def test_with_negative_number(self):
        self.assertFalse(
            get_sum_of_even_valued_fibonacci_terms_below_limit(-1), 0)

    def test_with_alphabetic_character(self):
        self.assertEqual(
            get_sum_of_even_valued_fibonacci_terms_below_limit('a'), 0)

    def test_with_special_character(self):
        self.assertFalse(
            get_sum_of_even_valued_fibonacci_terms_below_limit('#'))

    def test_without_parameter(self):
        with self.assertRaises(TypeError):
            get_sum_of_even_valued_fibonacci_terms_below_limit()


if __name__ == '__main__':
    unittest.main()
