n = int(input("input row count: "))
matrix = [list(input("input {0} row".format(i)).split(" ")) for i in range(n)]
for i in range(1, n):
    if matrix[i] == matrix[0]:
        print(i)
