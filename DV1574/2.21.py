def matrix_dimensions(matrix):

    first_row = len(matrix[0])
    ret_msg = "This is a %dx%d matrix." % (len(matrix), first_row)

    for a in range(1, len(matrix), 1):
        if first_row != len(matrix[a]):
            ret_msg = "This is not a valid matrix"
            a = len(matrix)
        
    return ret_msg


A = [[1, 3], [-5, 6], [2, 4], [1, 3], [-5, 6], [2, 4]]
B = [[1, 2, 3], [-5, 64]]
print(matrix_dimensions(A))