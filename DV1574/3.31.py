def two_factors(num):
    if num < 0:
        return "Invalid"
    elif num % 4 == 0:
        return f"2 * {two_factors(num/4)} * 2"
    elif num % 2 == 0:
        return f"2 * {two_factors(num/2)}"
    else:
        return f"{int(num)}"

print(two_factors(80))