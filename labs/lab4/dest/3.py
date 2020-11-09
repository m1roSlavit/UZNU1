from math import sqrt

x1 = float(input("input x1 value: "))
y1 = float(input("input y1 value: "))
x2 = float(input("input x2 value: "))
y2 = float(input("input y2 value: "))
x3 = float(input("input x3 value: "))
y3 = float(input("input y3 value: "))


def calculate_side_length(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


side1 = calculate_side_length(x1, y1, x2, y2)
side2 = calculate_side_length(x2, y2, x3, y3)
side3 = calculate_side_length(x3, y3, x1, y1)
result = max(side1, side2, side3)

print(result)
