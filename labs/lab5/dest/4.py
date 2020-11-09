n_number = int(input("input n: "))

def get_sequence_elem(i):
    if i == 0:
        return 1
    elif 1 <= i <= 3:
        return 7
    else:
        return (get_sequence_elem(i-1)*(1+get_sequence_elem(i-2)) + get_sequence_elem(i-3))/get_sequence_elem(i-4)


print("value of {0} = {1}" .format(n_number, get_sequence_elem(n_number)))
