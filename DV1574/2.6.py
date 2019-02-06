def count_vowels(string):
    counter = 0
    vowels = "aeiou"
    for a in string:
        if a in vowels:
            counter += 1
    return counter

print(count_vowels("apple"))