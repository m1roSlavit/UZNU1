import math


def get_vector_length(coords):
    return (coords[0]**2 + coords[1]**2)**(1/2)


def get_angle_from_vectors(x1, y1, x2, y2, x3, y3, x4, y4):
    first_vector = [x2-x1, y2-y1]
    second_vector = [x4-x3, y4-y3]
    vector_scalar = first_vector[0]*second_vector[0] + first_vector[1]*second_vector[1]
    return math.degrees(math.acos(vector_scalar/(get_vector_length(first_vector)*get_vector_length(second_vector))))


def get_type_of_triangle(x1, y1, x2, y2, x3, y3):
    angle_1 = get_angle_from_vectors(x1, y1, x2, y2, x1, y1, x3, y3)
    angle_2 = get_angle_from_vectors(x3, y3, x1, y1, x3, y3, x2, y2)
    angle_3 = get_angle_from_vectors(x2, y2, x1, y1, x2, y2, x3, y3)
    max_angle = max(angle_1, angle_2, angle_3)
    if max_angle > 90:
        return "obtuse"
    elif max_angle == 90:
        return "right"
    return "acute"


print(get_type_of_triangle(0, 0, 1, 7, 7, 1))

