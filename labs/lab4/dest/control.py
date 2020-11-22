x_value = float(input("input x value: "))
e_value = float(input("input e value"))

res = 0
n_c = 1
l_c = 1

while True:
    temp_value = l_c*((x_value**n_c)/n_c)
    l_c *= -1
    n_c += 1

    if abs(temp_value) < e_value:
        break
    res += temp_value

print(res)