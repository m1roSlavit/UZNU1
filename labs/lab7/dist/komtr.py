matrix = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]
n = len(matrix)

def is_matrix_sym(matrix, n):
    for i in range(n):
        for j in range(n - i - 1):
            if (matrix[i][j] != matrix[n - j - 1][n - i - 1]):
                return False
    return True

if (is_matrix_sym(matrix, n)):
    print("матриця симетрична відносно побічної діагоналі")
else:
    print("матриця не симетрична відносно побічної діагоналі")