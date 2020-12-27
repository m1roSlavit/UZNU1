import numbers

class TMan:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self.__name = val
        else:
            raise Exception('value of name must be str')

    @property
    def sex(self):
        return self.__name

    @sex.setter
    def sex(self, val):
        if val == "male" or val == "female":
            self.__sex = val
        else:
            raise Exception('value of sex must be male or female')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        if isinstance(val, numbers.Number) and val >= 0:
            self.__age = val
        else:
            raise Exception('value of age must be number')

    def get_type_of_age(self):
        if self.age < 12:
            return "дитиною"
        elif self.age < 18:
            return "юнаком"
        else:
            return "дорослою"

    def get_zodiac_sign(self, day, month):
        