
from ast import Try
import errno


def is_prime(number):
    try:
        if(number < 2):
            return False
        else:
            for quotient in range(2, number//2 + 1):
                if (number % quotient == 0):
                    return False

            else:
                return True

    except:
        return False
