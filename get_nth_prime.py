# https://projecteuler.net/problem=7
# 10001st prime

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from is_prime import is_prime


def get_nth_prime(limit):
    number = 1
    index = 0
    while(index < limit):
        number += 1
        if (is_prime(number) == True):            
            index += 1


    return number