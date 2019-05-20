def pattern(num):
    if num < 0:
        return "Invalid"
    elif num > 2:
        return f"<{pattern(num - 2)}>"
    else:
        return "*" * num

print(pattern(5))