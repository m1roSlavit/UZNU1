n_number = int(input("input n: "))

i = 4

x0 = 1
x1 = 7
x2 = 7
x3 = 7
res = 0

while i <= n_number:
    res = (x3*(1+x2)+x1)/x0
    x0, x1, x2, x3 = x1, x2, x3, res
    i += 1

print(res)
