import numbers

def sum_numbers(any_list):
    sum = 0
    for element in any_list: 
        if isinstance(element, numbers.Number):
            sum += element
    return sum

print(sum_numbers([1, 2, 3.2, 4, 5]))
print(sum_numbers(["a", 1, "b", 2, [["b", 4], 2], 3]))