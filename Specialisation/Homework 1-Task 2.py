import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Triangle perimeter: ", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_square(self):
        if self.a == self.b:
            raise ValueError("This is a square. Use the Square method")
        else:
            return False

    def calc_perimeter(self):
        self.is_square()
        perim = 2 * (self.a + self.b)
        print("Rectangle perimeter: ", perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def calc_perimeter(self):
        perim = 4 * self.a
        print("Square perimeter:", perim)
        return perim


my_triangle = Triangle(2, 2, 3)
my_triangle.calc_perimeter()

my_rectangle = Rectangle(2, 3)
my_rectangle.calc_perimeter()

my_square = Square(2)
my_square.calc_perimeter()