import random

n, m = map(int, input("input n m : ").split(" "))

matrix = [[random.randint(-100, 100) for i in range(n)] for x in range(m)]

matrix_col_char = []

for i in range(n):
    temp_val = 0
    temp_col = []
    for k in range(m):
        val = matrix[k][i]
        temp_col.append(val)
        if val < 0 and val % 2 != 0:
            temp_val += abs(val)
    matrix_col_char.append([temp_col, temp_val])

matrix_col_char.sort(key=lambda x: x[1])

new_matrix = [[matrix_col_char[k][0][i] for k in range(n)] for i in range(m)]

for i in range(m):
    print(new_matrix[i])

