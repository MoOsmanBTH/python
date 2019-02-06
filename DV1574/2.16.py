def sum_last_digits(a_list):
    sum = 0
    for a in a_list:
        sum += a % 10
    return sum

print(sum_last_digits([123, 23, 541, 2 ,1]))