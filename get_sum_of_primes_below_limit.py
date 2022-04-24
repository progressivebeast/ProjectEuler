# https://projecteuler.net/problem=10
# Summation of primes

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from is_prime import is_prime


def get_sum_of_primes_below_limit(limit):
    summa = 0
    try:
        for x in range(1, limit):
            if (is_prime(x) == True):
                summa += x

        return summa
    except:
        print('Parameter limit must be a number!')

    finally:
        return summa
