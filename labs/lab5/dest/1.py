from math import sin
n_number = int(input("input n: "))
x_val = float(input("input x value(rad): "))
total_result = 0
for i in range(n_number):
    total_result += sin(x_val)**i

print("result: ",total_result)
