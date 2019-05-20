def all_pairs(my_list):
    tuple_list = []

    for x in my_list:
        for y in my_list:
            tuple_list.append((x, y))
    
    return tuple_list
