def invert_dictionary(dictionary):
    inv_dictionary = {}
    
    for a in dictionary.keys():
        if dictionary[a] in inv_dictionary.keys():
            inv_dictionary[dictionary[a]].append(a)
        else:
            inv_dictionary[dictionary[a]] = [a]
    return inv_dictionary

print(invert_dictionary({'a':1, 'b':2, 'c':3, 'd':2}))