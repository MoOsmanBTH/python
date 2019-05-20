def sort_by_len(tup, direction):
    ret_tup = [a for a in tup]

    if direction == "asc":
        ret_tup.sort(key= len)
    elif direction == "des":
        ret_tup.sort(key= len, reverse = True)

    return tuple(ret_tup)

print(sort_by_len(('Windows', 'Linux', 'OSX'), 'des'))
print(sort_by_len(('apple', 'orange', 'pear'), 'des'))