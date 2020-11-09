import math

side_length = float(input("Input side length: "))
angle_value = float(input("Input angle value: "))

rhomb_P = 4*side_length
rhomb_S = math.sin(math.radians(angle_value))*side_length*side_length

print("P: {0}, S: {1}" .format(rhomb_P, rhomb_S))
