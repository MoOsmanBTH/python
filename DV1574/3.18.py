def  dict_to_list(vector):
    ret_list = [0 for _ in range(0, list(vector.keys())[-1] + 1)]
    for a in vector.keys():
        ret_list[a] = vector[a]
    return ret_list

print(dict_to_list({0: 1, 3: 2, 7: 3, 12: 4}))