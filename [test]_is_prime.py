import unittest
from is_prime import is_prime


class Test_is_prime(unittest.TestCase):

    def test_True(self):
        self.assertTrue(is_prime(3))

    def test_False(self):
        self.assertFalse(is_prime(4))

    def test_with_negative_number(self):
        self.assertFalse(is_prime(-1))

    def test_with_alphabetic_character(self):
        self.assertFalse(is_prime('a'))

    def test_with_special_character(self):
        self.assertFalse(is_prime('#'))

    def test_without_parameter(self):
        with self.assertRaises(TypeError):
            is_prime()


if __name__ == '__main__':
    unittest.main()
