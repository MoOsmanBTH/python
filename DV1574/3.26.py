def add_dashes(word):
    if len(word) <= 0:
        return "None"
    elif len(word) == 1:
        return word
    else:
        return word[0] + "-" + add_dashes(word[1:])

print(add_dashes(""))