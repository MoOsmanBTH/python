def is_prime(number):
    for i in range(1, number, 1):
       checkPrime = True
       if number % i == 0:
           checkPrime = False
           i = number
    return checkPrime
           