def sum_digits(digits):
    if digits > 0:
        return digits % 10 + sum_digits(int(digits / 10))
    else:
        return 0

print(sum_digits(1234))