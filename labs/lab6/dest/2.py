import math

x = float(input("input x value: "))
i = int(input("input i value: "))
integral = 1
previous_element = 1
all_elements = []
sign = 1

i_counter = 1
while i_counter <= i:
    integral *= i_counter
    elem = previous_element + sign*math.sin(i_counter*x)*math.cos(integral*x)
    previous_element = elem
    all_elements.append(elem)
    sign *= -1
    i_counter += 1

print(all_elements)

max_elem_index = 0

for i in range(len(all_elements)):
    if all_elements[i] > all_elements[max_elem_index]:
        max_elem_index = i

res = max_elem_index + 1
print(res)
