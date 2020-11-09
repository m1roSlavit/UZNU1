# from math import pi, sin, fabs
#
# x_value = float(input("input x value: "))
# E_val = float(input("input E value: "))
#
# equation_left_part = sin(x_value)
# equation_right_part = x_value*(1-(x_value**2)/(pi**2))*(1-(x_value**2)/(4*(pi**2)))
#
# n_counter = 0
#
# while fabs(equation_right_part) > E_val:
#     temp_val = 1 - (x_value**2)/(pi**2 * (n_counter-1)**2)
#     n_counter += 3
#     print(temp_val)
#     print(equation_right_part)
#     equation_right_part *= temp_val
#
# print(equation_left_part, equation_right_part)

# n_number = int(input("input n: "))
#
# def get_sequence_elem(i):
#     if i == 0:
#         return 1
#     elif 1 <= i <= 3:
#         return 7
#     else:
#         return (get_sequence_elem(i-1)*(1+get_sequence_elem(i-2)) + get_sequence_elem(i-3))/get_sequence_elem(i-4)
#
#
# print("value of {0} = {1}" .format(n_number, get_sequence_elem(n_number)))

# from math import sin
# n_number = int(input("input n: "))
# x_val = float(input("input x value(rad): "))
# total_result = 0
# for i in range(n_number):
#     total_result += sin(x_val)**i
#
# print("result: ",total_result)

# from functools import reduce
#
# amount_of_numbers = int(input("input amount of numbers: "))
# all_numbers = []
# for i in range(amount_of_numbers):
#     all_numbers.append(float(input("input number {} : " .format(i+1))))
#
# average_val = reduce(lambda x, y: x + y, all_numbers)/amount_of_numbers
#
# num_counter = 0
#
# for i in range(amount_of_numbers):
#     if all_numbers[i] < average_val:
#         num_counter += 1
#
# print("Result: ", num_counter)


