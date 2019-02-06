def get_char(string, position):
    ret_val = "Invalid position."
    if string.count(string) >= position:
        ret_val = string[position]
    
    return ret_val

word = "giraffe"
print(get_char(word, 6))