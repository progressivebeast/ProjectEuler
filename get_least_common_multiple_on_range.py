# https://projecteuler.net/problem=5
# Smallest multiple

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from get_prime_factors import get_prime_factor_dictionary

def get_least_common_multiple_on_range(start, end):

    prime_factors = {}
    least_common_multiple = 1

    for x in range(start,end+1):
        actual_prime_factors = get_prime_factor_dictionary(x)        
        for factor in actual_prime_factors.keys():
            if factor in prime_factors:
                if prime_factors[factor] < actual_prime_factors[factor]:
                    prime_factors.update({factor: actual_prime_factors[factor]})
            else:
                prime_factors.update({factor: actual_prime_factors[factor]})

    for x in prime_factors:
        least_common_multiple *= x ** prime_factors[x]
    
    return least_common_multiple