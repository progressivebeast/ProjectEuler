# https://projecteuler.net/problem=9
# Special Pythagorean triplet

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a,b,c):
    numbers = [a,b,c]
    numbers.sort()    

    if (numbers[2] ** 2 == numbers[1] ** 2 + numbers[0] ** 2):
        return True
    else:
        return False

def get_pythagorean_triplet_product_by_sum(summa):
    for a in range(1, summa):
        for b in range(a + 1, summa - a):
            if (is_pythagorean_triplet(summa - b - a, b, a)):
                return a * b * (summa - b -a)



print(get_pythagorean_triplet_product_by_sum(1000))        
