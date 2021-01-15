class TPTriangle:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def s(self):
        return self.a * self.b / 2

    @a.setter
    def a(self, value):
        value = int(value)
        if value <= 0:
            raise Exception('error')
        else:
            self.__a = value

    @b.setter
    def b(self, value):
        if value <= 0:
            raise Exception('error')
        else:
            self.__b = value

    def square(self):
        return self.s

    def perrimeter(self):
        return self.a + self.b + (self.a ** 2 + self.b ** 2) ** 0.5

    def __add__(self, other):
        return TPTriangle(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return TPTriangle(self.a * other.a, self.b * other.b)

    def __sub__(self, other):
        return TPTriangle(self.a - other.a, self.b - other.b)

    def __lt__(self, other):
        return self.s < other.s

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __gt__(self, other):
        return self.s > other.s

    def __le__(self, other):
        return self.s <= other.s

    def __ge__(self, other):
        return self.s >= other.s


class TPPiramid(TPTriangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    @property
    def v(self):
        return super().square() * self.h / 3

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        if value <= 0:
            raise Exception('error')
        else:
            self.__h = value

    def __add__(self, other):
        return TPPiramid(self.a + other.a, self.b + other.b, self.h + other.h)

    def __mul__(self, other):
        return TPPiramid(self.a * other.a, self.b * other.b, self.h * other.h)

    def __sub__(self, other):
        return TPPiramid(self.a - other.a, self.b - other.b, self.h - other.h)

    def volume(self):
        return self.v

    def __lt__(self, other):
        return self.v < other.v

    def __eq__(self, other):
        return self.v == other.v

    def __ne__(self, other):
        return self.v != other.v

    def __gt__(self, other):
        return self.v > other.v

    def __le__(self, other):
        return self.v <= other.v

    def __ge__(self, other):
        return self.v >= other.v