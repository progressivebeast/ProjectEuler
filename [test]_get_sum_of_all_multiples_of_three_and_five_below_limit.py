import unittest
from get_sum_of_all_multiples_of_three_and_five_below_limit import get_sum_of_all_multiples_of_three_and_five_below_limit


class Test_get_sum_of_all_multiples_of_three_and_five_below_limit(unittest.TestCase):

    def test_positive_branch(self):
        self.assertEqual(
            get_sum_of_all_multiples_of_three_and_five_below_limit(10), 23)

    def test_negative_branch(self):
        self.assertNotEqual(
            get_sum_of_all_multiples_of_three_and_five_below_limit(10), 45)

    def test_with_negative_number(self):
        self.assertEqual(
            get_sum_of_all_multiples_of_three_and_five_below_limit(-10), 0)

    def test_with_alphabetic_character(self):
        self.assertEqual(
            get_sum_of_all_multiples_of_three_and_five_below_limit('a'), 0)

    def test_with_special_character(self):
        self.assertEqual(
            get_sum_of_all_multiples_of_three_and_five_below_limit('#'), 0)

    def test_without_parameter(self):
        with self.assertRaises(TypeError):
            get_sum_of_all_multiples_of_three_and_five_below_limit()


if __name__ == '__main__':
    unittest.main()
