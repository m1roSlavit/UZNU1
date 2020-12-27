class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def g(self):
        return self.a + self.b

    def __str__(self):
        return "{0} {1} {2}".format(self.a, self.b, self.c)

print(Vector(1, 2, 3).g())