import numbers

class TArProgression:
    def __init__(self, first_elem, d_value):
        self.first_elem = first_elem
        self.d_value = d_value

    @property
    def first_elem(self):
        return self.__first_elem

    @first_elem.setter
    def first_elem(self, value):
        if isinstance(value, numbers.Number):
            self.__first_elem = float(value)
        else:
            raise Exception('first elem value must be number')

    @property
    def d_value(self):
        return self.__d_value

    @d_value.setter
    def d_value(self, value):
        if isinstance(value, numbers.Number):
            self.__d_value = float(value)
        else:
            raise Exception('value of d must be number')

    def input_value_of_first_elem(self):
        self.first_elem = float(input("input first elem value: "))

    def input_value_of_d(self):
        self.d_value = float(input("input d value: "))

    def print_values(self):
        print("first elem: {0}, d value: {1};".format(self.first_elem, self.d_value))

    def get_value_of_elem(self, n):
        return self.first_elem + (n-1)*self.d_value

    def get_sum_of_elements(self, n):
        return ((self.first_elem + self.get_value_of_elem(n))/2)*n

    def __add__(self, other):
        return TArProgression(self.first_elem+other.first_elem, self.d_value+other.d_value)

    def __sub__(self, other):
        return TArProgression(self.first_elem - other.first_elem, self.d_value - other.d_value)

class TArProgressionM(TArProgression):
    def __init__(self, first_elem, d_value):
        super().__init__(first_elem, d_value)

    def is_sequence_of_numbers_arithmetic_progression(self, sequence):
        d_val = sequence[1]-sequence[0]
        prev_val = sequence[1]
        for elem in sequence[2:]:
            if(elem-prev_val != d_val):
                return False
            prev_val = elem
        return True

    def is_number_in_sequence(self, value):
        n_val = (value-self.first_elem+self.d_value)/self.d_value
        if int(n_val) == n_val:
            return True
        else:
            return False


firstSeq = TArProgression(5, 3)
secondSeq = TArProgression(1, 2)

subSeq = firstSeq - secondSeq
sumSeq = firstSeq + secondSeq

sumSeq.print_values()
subSeq.print_values()

testNewSeq = TArProgressionM(1, 2)
print(testNewSeq.is_sequence_of_numbers_arithmetic_progression([1, 2, 3, 4]))

print(testNewSeq.is_number_in_sequence(2))

print(firstSeq.first_elem, firstSeq.d_value, firstSeq.get_sum_of_elements(5))