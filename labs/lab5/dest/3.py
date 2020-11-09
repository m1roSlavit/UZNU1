from math import pi, sin, fabs

x_value = float(input("input x value: "))
E_val = float(input("input E value: "))

static_value = (x_value**2)/(pi**2)

res = x_value

n_counter = 2

while True:
    temp_val = 1 - static_value/((n_counter - 1)**2)
    n_counter += 1
    if fabs(temp_val) < E_val:
        break
    res *= temp_val

print(res)