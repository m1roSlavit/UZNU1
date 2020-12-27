class Straight_on_the_set:
    def __init__(self, guide_vector, dot):
        self.guide_vector = guide_vector
        self.dot = dot

    def input_data(self):
        self.guide_vector = list(input("input guide vector").split(","))
        self.dot = input("input dot").split(",")

    def print_data(self):
        print("guide vector: {0}; dot: {1};".format(self.guide_vector, self.dot))

    def point_of_intersection(self, other):
        m = self.guide_vector[0]
        n = self.guide_vector[1]
        m1 = other.guide_vector[0]
        n1 = other.guide_vector[1]
        x0 = self.dot[0]
        y0 = self.dot[1]
        x01 = other.dot[0]
        y01 = other.dot[1]
        x = (m*x01*n1-y01*m1*m+y0*m*m1-x0*n*m1)/(m*n1-n*m1)
        y = (x*n-x0*n+y0*m)/m
        return [x, y]

    def is_paralel(self, other):
        return self.guide_vector[0]/other.guide_vector[0] == self.guide_vector[1]/other.guide_vector[1]

    def is_dot_belong(self, other_dot):
        return (other_dot[0] - self.dot[0])/self.guide_vector[0] == (other_dot[1] - self.dot[1])/self.guide_vector[1]


test1 = Straight_on_the_set([1, 1], [3, 7])
test2 = Straight_on_the_set([2, 4], [2, 9])
print(test1.is_dot_belong([0, 6]))