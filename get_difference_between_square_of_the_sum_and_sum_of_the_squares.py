# https://projecteuler.net/problem=6
# Sum square difference

# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)**2 = 55**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def get_difference_between_square_of_the_sum_and_sum_of_the_squares(start, end):
    sum_of_the_squares = 0
    squares_of_the_sum = 0
    for num in range(start, end + 1):
        sum_of_the_squares += num ** 2
        squares_of_the_sum += num

    squares_of_the_sum = squares_of_the_sum ** 2
    
    return (squares_of_the_sum - sum_of_the_squares)
    