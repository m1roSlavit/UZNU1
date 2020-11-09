number = float(input("pls type number: "))

if 0 <= number < 5:
    result = 0
elif 5 <= number < 10:
    result = 1
elif 10 <= number < 15:
    result = 2
else:
    result = 3

print("result", result)
