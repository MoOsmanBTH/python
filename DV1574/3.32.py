def pascal(k,i):
    if k < 0 or i < 0 or i > k:
        return 0
    elif k == 0 or i == 0:
        return 1
    else:
        return pascal(k - 1, i - 1) + pascal(k - 1, i)

print(pascal(5, 3))