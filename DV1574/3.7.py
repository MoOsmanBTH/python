def not_common(tup1, tup2): 
    ret_tup = []
    for a in tup1:
        if a not in tup2 and a not in ret_tup:
            ret_tup.append(a)
    for b in tup2:
        if b not in tup1 and b not in ret_tup:
            ret_tup.append(b)
    return tuple(ret_tup)

print(not_common((1, 2, 3, 4), (3, 4, 5, 6)))

print(not_common(('b', 'a', 'c', 'd'), ('a', 'b', 'c')))

print(not_common(('a', 'b', 'c'), ('a', 'b', 'c')))