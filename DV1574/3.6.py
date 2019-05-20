def common_content(tup1, tup2):
    ret_tup = []
    for a in tup1:
        if a in tup2 and a not in ret_tup:
            ret_tup.append(a)
    return tuple(ret_tup)

print(common_content((1, 3, "p", "n"), ("a", 2, 5, 1, 1, "p")))