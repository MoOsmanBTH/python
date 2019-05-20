def sum_all(int_num): 
    if int_num < 0:
        return "Invalid"
    elif int_num == 0:
        return 0
    else:
        return int_num + sum_all(int_num - 1)

print(sum_all(10))