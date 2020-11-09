from functools import reduce

amount_of_numbers = int(input("input amount of numbers: "))
all_numbers = []
for i in range(amount_of_numbers):
    all_numbers.append(float(input("input number {} : " .format(i+1))))

average_val = reduce(lambda x, y: x + y, all_numbers)/amount_of_numbers

num_counter = 0

for i in range(amount_of_numbers):
    if all_numbers[i] < average_val:
        num_counter += 1

print("Result: ", num_counter)
