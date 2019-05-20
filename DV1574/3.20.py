def power(base, exp):
    if exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1

print(power(5,2))