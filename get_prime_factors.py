from is_prime import is_prime

def get_prime_factor_list(number):
    prime_factor_list = []

    while(number != 1):
        for quotient in range(1, number//2 + 1):
            if (number % quotient == 0 and is_prime(quotient) == True):
                prime_factor_list.append(quotient)
                number = number // quotient
                break
            elif (is_prime(number) == True):
                prime_factor_list.append(number)
                number = 1
                break

    return prime_factor_list

def get_prime_factor_dictionary(number):
    prime_factor_dictionary = {}

    for x in get_prime_factor_list(number):
        if x in prime_factor_dictionary:
            prime_factor_dictionary.update({x: prime_factor_dictionary[x] + 1})
        else:
            prime_factor_dictionary.update({x: 1})

    return prime_factor_dictionary