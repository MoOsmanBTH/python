def numbers_between(start, end):
    if start == end:
        return f"{start}"
    else:
        return f"{start}," + numbers_between(start + 1, end)

print(numbers_between(7, 11))