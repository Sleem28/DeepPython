from Matrix import Matrix


if __name__ == '__main__':

    mat1 = [[3, 5, 8], [6, 8, 9], [2, 5, 9]]
    mat2 = [[3, 5, 8], [6, 8, 9], [2, 5, 9]]
    mat3 = [[3, 5, 2], [6, 8, 9], [2, 5, 9]]
    bad_mat = [[3, 5], [6, 8, 9], [2, 5, 9]]

    matrix1 = Matrix(mat1)
    matrix2 = Matrix(mat2)
    matrix3 = Matrix(mat3)
    bad_matrix = Matrix(bad_mat)

    print(bad_matrix)
    print(matrix1)
    print(matrix3)
    print(matrix1 == matrix3)
    print(matrix1 + matrix3)
    print(matrix1 * matrix3)


