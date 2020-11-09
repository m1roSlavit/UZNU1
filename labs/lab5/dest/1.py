from math import sin
n_number = int(input("input n: "))
x_val = float(input("input x value(rad): "))
total_result = 0
i_c = 0
while i_c < n_number:
    total_result += sin(x_val)**i_c
    i_c += 1

print("result: ", total_result)
