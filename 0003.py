# https://projecteuler.net/problem=3
# Largest prime factor

# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def isPrime(number):
    for quotient in range(2, number//2 + 1):
        if (number % quotient == 0):
            return False
    else:
        return True


def getPrimeFactors(number):
    primeFactors = []

    while(number != 1):
        for quotient in range(2, number//2 + 1):
            if (number % quotient == 0 and isPrime(quotient) == True):
                primeFactors.append(quotient)
                number = number // quotient
                break
            elif (isPrime(number) == True):
                primeFactors.append(number)
                number = 1
                break

    return primeFactors


print(max(getPrimeFactors(600851475143)))
