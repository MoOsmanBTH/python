def above_average(num_list):
    return [a for a in num_list if a > sum(num_list)/len(num_list)]

num_list = [1, 2, 3, 8, 10]
print(above_average(num_list))