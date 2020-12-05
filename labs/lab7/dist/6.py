# ------- random
# import random
#
# n = int(input("input n: "))
# matrix = [[random.randint(-10, 100) for i in range(n)] for x in range(n)]

# ------- test
matrix = [[-1, 2, 3], [2, -5, 8], [3, 8, 4]]
n = 3

for i in range(n):
    for k in range(n):
        if matrix[k][i] < 0:
            temp_arr = []
            for j in range(n):
                temp_arr.append(matrix[j][i])
            if temp_arr == matrix[i]:
                print("sum of {0} col: {1}".format(i+1, sum(temp_arr)))
            break
