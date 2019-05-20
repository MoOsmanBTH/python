def count_X(string):
    if string == "":
        return 0
    elif string[0] == "X":
        return 1 + count_X(string[1:])
    else:
        return count_X(string[1:])

print(count_X("Xilinx"))