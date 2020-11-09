number_a = float(input("input value of a: "))
number_b = float(input("input value of b: "))
number_c = float(input("input value of c: "))

result = (number_a if number_a < number_b else number_b) + (number_a if number_a > number_b else number_b)**2

print("your result is number: ", result)
