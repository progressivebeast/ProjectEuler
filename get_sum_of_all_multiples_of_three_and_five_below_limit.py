# https://projecteuler.net/problem=1
# Multiples of 3 or 5

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


# With natural way

limit = 1000
counter = 1
summa = 0
while(counter < limit):
    if(counter % 3 == 0 or counter % 5 == 0):
        summa += counter
    counter += 1

print(summa)


# With list comprehension

def get_sum_of_all_multiples_of_three_and_five_below_limit(limit):
    return sum([x for x in list(range(1,limit)) if x % 3 == 0 or x % 5 == 0])
