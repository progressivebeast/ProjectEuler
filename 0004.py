# https://projecteuler.net/problem=4
# Largest palindrome product

# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

for a in range(100, 1000):
    for b in range(100, 1000):
        if(str(a*b) == str(a*b)[::-1]):
            palindrome = str(a) + ' * ' + str(b) + ' = ' + str(a*b)

print(palindrome)
