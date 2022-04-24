import unittest
from get_sum_of_primes_below_limit import get_sum_of_primes_below_limit


class Test_get_sum_of_primes_below_limit(unittest.TestCase):

    def test_with_number(self):
        self.assertEqual(get_sum_of_primes_below_limit(10), 17)

    def test_with_negative_number(self):
        self.assertEqual(get_sum_of_primes_below_limit(-4), 0)

    def test_with_first_prime(self):
        self.assertEqual(get_sum_of_primes_below_limit(2), 0)

    def test_with_alphabetic_character(self):
        self.assertEqual(get_sum_of_primes_below_limit('a'), 0)

    def test_with_special_character(self):
        self.assertEqual(get_sum_of_primes_below_limit('#'), 0)

    def test_without_parameter(self):
        with self.assertRaises(TypeError):
            get_sum_of_primes_below_limit()


if __name__ == '__main__':
    unittest.main()
