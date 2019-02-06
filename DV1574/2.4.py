def search(string, sub_string):
    ret_value = -1
    if string.find(sub_string):
        ret_value = string.index(sub_string)
    return ret_value

print(search("elephant", "ant"))