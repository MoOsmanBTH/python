def count_char(string, char):
    counter = 0
    for i in string:
        if i == char:
            counter += 1
    return counter

print(count_char(input("String: "), input("Char: ")))