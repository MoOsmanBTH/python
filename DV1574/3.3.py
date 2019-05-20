def unordered_pairs(my_list):
    tuple_list = []

    for x in range(0, len(my_list)):
        for y in range(x, len(my_list)):
            tuple_list.append((my_list[x], my_list[y]))
    
    return tuple_list
