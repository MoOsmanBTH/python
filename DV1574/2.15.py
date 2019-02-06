def find_letter(char, a_list):
    char_exist = False
    for a in a_list:
        if a == char:
            char_exist = True
    return char_exist

print(find_letter("u", ["h", "o", "u", "s", "e"]))
print(find_letter("b", ["c", "a", "r"]))