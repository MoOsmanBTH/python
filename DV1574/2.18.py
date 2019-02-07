def distribute(my_item, my_list):
    new_list = []
    for a in range(0, len(my_list), 1):
        new_list.append(my_list[a])
        new_list[a].append(my_item)
    return new_list

old_list = ["kangar"], ["z"], ["f"]
print(distribute("oo", old_list))