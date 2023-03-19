# Напишите функцию для транспонирования матрицы
def matrix_transponder(matrix: list) -> list:
    rows = len(matrix)
    columns = len(matrix[0])
    result_matrix = [[0]*rows for i in range(columns)]

    for i in range(rows):
        for j in range(columns):
            result_matrix[j][i] = matrix[i][j]
    return result_matrix

def print_matrix(matrix: list):
    for row in matrix:
        print(row)

my_matrix = [[1, 5, 12], [2, -3, 25]] 

print('The matrix before transponding looks like:')
print_matrix(my_matrix)
print('\nThe matrix after transponding looks like:')
print_matrix(matrix_transponder(my_matrix))


    