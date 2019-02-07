def extended_each(my_item, my_list):
    for a in range(0, len(my_list), 1):
        my_list[a].append(my_item)

old_list = ["kangar"], ["z"], ["f"]
extended_each("oo", old_list)
print(old_list)