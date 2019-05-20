def same_content(tup1, tup2):
    ret_val = True
    if len(tup1) != len(tup2):
        ret_val = False
    else:
        for a in range(0, len(tup1)):
            if tup1[a] != tup2[a]:
                ret_val = False
    
    return ret_val

print(same_content((1, 2), ()))