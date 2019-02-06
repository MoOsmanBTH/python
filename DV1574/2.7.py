def palindrom(string):
    ret_value = "%s is not a palindrome.\n" % (string)

    if string.lower() == string[::-1].lower():
        ret_value = "%s is a palindrome.\n" % (string)
    return ret_value.capitalize()

user_input = ""

while user_input != "quit":
    user_input = input("Write a word: ")
    if user_input == "quit":
        print("Exiting ...")
    else:
        print(palindrom(user_input))