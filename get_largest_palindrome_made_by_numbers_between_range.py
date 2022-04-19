# https://projecteuler.net/problem=4
# Largest palindrome product

# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def get_largest_palindrome_made_by_numbers_between_range(start, end):
    for a in range(start, end):
        for b in range(start, end):
            if(str(a*b) == str(a*b)[::-1]):
                palindrome = str(a) + ' * ' + str(b) + ' = ' + str(a*b)

    return palindrome
