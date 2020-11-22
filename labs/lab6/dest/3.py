a_v = [float(x) for x in input("введіть через пробіл координати вектора a: ").split(" ")]
b_v = [float(x) for x in input("введіть через пробіл координати вектора b: ").split(" ")]
c_v = [float(x) for x in input("введіть через пробіл координати вектора c: ").split(" ")]


def calculate_scalar(a, b):
    if len(a) == len(b):
        res = 0
        for i in range(len(a)):
            res += a[i]*b[i]
        return res


res = 2*calculate_scalar(a_v, b_v)-3*calculate_scalar(a_v, c_v)

print(res)
