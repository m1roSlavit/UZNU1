import random

n, m = map(int, input("input n m : ").split(" "))

matrix_a = [[random.randint(-100, 100) for i in range(n)] for x in range(m)]

new_matrix = [[matrix_a[k][j] for k in range(m)] for j in range(n)]

print(new_matrix)