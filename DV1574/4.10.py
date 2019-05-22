def validate_mail(string):
    check = False
    if "@" in string and "." in string[-4:]:
        check = True
    if check:
        for a in range(0, string.find("@")):
            if not ("a" <= string[a].lower() <= "z" or "0" <= string[a] <= "9" or string[a] == "-" or string[a] == "_"):
                check = False
        for a in range(string.find("@") + 1, string.find(".")):
            if not "a" <= string[a].lower() <= "z":
                check = False
        if len(string) - string.find(".") > 4:
            check = False
    return check

email_file = open("emails.txt", "r")
unfiltered_list = [a.strip("\n") for a in email_file]
email_file.close()

filtered_list = list(filter(validate_mail, unfiltered_list))
print(filtered_list)