def transpose(matrix):
    column = len(matrix)
    row = len(matrix[0])
    
    matrix_t = True
    for a in range(1, column, 1):
        if row != len(matrix[a]):
            matrix_t = False
            a = column

    if matrix_t:    
        matrix_t  = [[matrix[a][b] for a in range(0, column, 1)]for b in range(0, row, 1)]
    return matrix_t

A = [[1,2,3],[4,5,6]]
print(transpose(A))