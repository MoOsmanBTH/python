def calculate_pascal(k, i):
    if k < 0 or i < 0 or i > k:
        return 0
    elif k == 0 or i == 0:
        return 1
    else:
        return calculate_pascal(k - 1, i - 1) + calculate_pascal(k - 1, i)

def pascal(n):
    return [[calculate_pascal(a, b)for b in range(a + 1)]for a in range(n)]

print(pascal(4))