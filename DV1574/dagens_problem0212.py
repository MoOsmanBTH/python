text = ["0"]
i = 0

while text[i] != "q":
    text.append(input("row: "))
    i += 1

    char_counter = 0 
    for a in text[i]:
        char_counter += 1

    indentation = ""
    if char_counter == 0 or char_counter > 40:
        text.pop(i)
        i += -1
    elif text[i] != "q":
        for _ in range (0, 40 - char_counter, 1):
            indentation += " "
        text[i] = indentation + text[i]

for b in range(1, i, 1):
    print(text[b])









# for a in text:
#     if a != "\n": 
#         char_counter += 1
#     else: 
#         forbidden_chars += 1


# indentation = ""
# if char_counter > 0 and forbidden_chars == 0:
#     for _ in range(0, 40 - char_counter, 1):
#         indentation += " "