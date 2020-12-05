import random

res = 1

n = int(input("input matrix size n: "))
m = int(input("input matrix size m: "))

matrix = [[random.randint(-100, 100) for i in range(n)] for x in range(m)]
for i in range(m):
    for k in range(i if i < n else n):
        res *= matrix[i][k]

print(res)