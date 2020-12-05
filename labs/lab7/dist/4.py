import random

n = int(input("input n: "))
matrix = [[random.randint(-100, 100) for i in range(n)] for x in range(n)]

for i in range(n):
    if i % 2 == 0: #тут або != 0 або == 0 взалежносі з якого числа починається з 0 або з 1
        temp_arr = []
        for k in range(n):
            temp_arr.append(matrix[k][i])
        temp_arr.sort(reverse=True)
        for k in range(n):
            matrix[k][i] = temp_arr[k]

print(matrix)