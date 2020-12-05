import math

n = int(input("input matrix size: "))

matrix = [[math.sin(((i+1)**2 - (j+1)**2)/n) for i in range(n)] for j in range(n)]

maxElem = [matrix[0][0], 0, 0]

for j in range(n):
    for i in range(n):
        if abs(matrix[j][i]) > maxElem[0]:
            maxElem[0] = matrix[j][i]
            maxElem[1] = j
            maxElem[2] = i

print("max = {0}; elem i = {1}; j={2}".format(maxElem[0], maxElem[1], maxElem[2]))