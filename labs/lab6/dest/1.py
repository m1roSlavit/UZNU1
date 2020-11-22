vector = [float(x) for x in input("ВВедіть координати черерез пробіл: ").split(" ")]
res = 1
for x in vector:
    if x < 0:
        res *= x

print(res)
