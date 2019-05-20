def sort_by_number(tup_list):
    tup_list.sort(key = lambda tup: tup[0])
    ret_tup = [a[1] for a in tup_list]

    # for a in range(0, len(tup_list)):
    #     ret_tup[tup_list[a][0] - 1] = tup_list[a][1]

    return tuple(ret_tup)

print(sort_by_number([(6, 'DV1574'), (4, 'Python'), (5, 'course'), (1, 'Welcome'), (3, 'the'), (2, 'to')]))