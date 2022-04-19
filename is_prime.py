
def is_prime(number):
    if(number < 2):
            return False
    else:            
        for quotient in range(2, number//2 + 1):        
            if (number % quotient == 0):
                return False
            
        else:
            return True