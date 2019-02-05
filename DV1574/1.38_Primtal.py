def is_prime(number):
    checkPrime = True
    if number <= 1:
        checkPrime = False
    else:
        for i in range(2, number, 1):
            if number % i == 0:
                checkPrime = False
                i = number
    return checkPrime

user_input = int(input("is it prime: "))
print(is_prime(user_input))