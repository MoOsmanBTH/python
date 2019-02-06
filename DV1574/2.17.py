def add_first_and_last(a_list):
    sum = 0
    if len(a_list) == 1:
        sum = a_list[0]
    if len(a_list) > 1:
        sum = a_list[0] + a_list[len(a_list) - 1]
    return sum

print(add_first_and_last([2, 7 , 4, 3]))