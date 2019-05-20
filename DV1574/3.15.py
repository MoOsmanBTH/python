def reverse_lookup(dictionary , value):
    ret_list = []

    for a in dictionary.keys():
        if dictionary[a] == value:
            ret_list.append(a)
    return ret_list

print(reverse_lookup({'a':1, 'b':2, 'c':2}, 2))