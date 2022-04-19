# https://projecteuler.net/problem=3
# Largest prime factor

# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from get_prime_factors import get_prime_factor_list

def get_largest_prime_factor(number):
    return max(get_prime_factor_list(number))
