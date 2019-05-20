def is_palindrome(word):
    if word == "":
        return True
    elif word[0].lower() == word[-1].lower():
        return is_palindrome(word[1:-1])
    else:
        return False

print(is_palindrome("Racecar"))