from math import pi, sin, fabs

x_value = float(input("input x value: "))
E_val = float(input("input E value: "))

equation_left_part = sin(x_value)
equation_right_part = x_value*(1-(x_value**2)/(pi**2))*(1-(x_value**2)/(4*pi**2))

n_counter = 6

while True:
    temp_val = equation_right_part*(1 - (x_value**2)/(pi**2 * (n_counter-1)**2))
    n_counter += 1
    print(temp_val)
    if fabs(temp_val) < E_val:
        break
    equation_right_part = temp_val

if equation_left_part == equation_right_part:
    print("Рівність справедлива")
else:
    print("Рівність несправидлива")