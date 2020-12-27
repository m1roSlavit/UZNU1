class TArray:
    def __init__(self, array):
        self.array = array
        self.array_elem_count = len(array)+1

    def input_data(self):
        self.array = list(input("input new array").split(","))
        self.array_elem_count = len(self.array)+1

    def print_data(self):
        print("array: {0}; elem count: {1};".format(self.array, self.array_elem_count))

    def get_min(self):
        return min(self.array)

    def get_max(self):
        return max(self.array)

    def sort_arr(self):
        self.array.sort()

    def get_sum(self):
        return sum(self.array)

    def __add__(self, other):
        return [self.array[i] + other.array[i] for i in range(len(self.array))]

    def __sub__(self, other):
        return [self.array[i] - other.array[i] for i in range(len(self.array))]

    def __mul__(self, other):
        return [el*other for el in self.array]

test1 = TArray([1, 2, 4, 5])
test2 = TArray([1, 3, 2, 12])

print(test1*2)