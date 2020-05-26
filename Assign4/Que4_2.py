from abc import ABC, abstractmethod


#Base classes and derived classes forming hierarchy

# Base  classes
class Shapes(ABC):
    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_fill(self):
        return self.__filled

    def set_fill(self, filled):
        self.__filled = filled

    # abstract methods        
    @abstractmethod
    def area(self):
        pass
        

    def perimeter(self):
        pass

#polymorphism of functions like perimeter()
#overrides baseclass methods in functionality
# Derived Classes
class Rectangle(Shapes):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def print_dimension(self):
        print("The length and breadth are", self.__length, "and", self.__breadth)

    def area(self):
        print("Area is", self.__length * self.__breadth)

    def perimeter(self):
        print("Perimeter is", 2 * (self.__length + self.__breadth))


class Square(Shapes):
    def __init__(self, lengthofside):
        super().__init__()
        self.__lengths = lengthofside

    def print_dimension(self):
        print("The length of side is", self.__lengths)

    def area(self):
        print("Area is", self.__lengths * self.__lengths)

    def perimeter(self):
        print("Perimeter is", 4 * self.__lengths)


class Triangle(Shapes):

    def __init__(self, length):
        super().__init__()
        self.__length = length

    def print_dimension(self):
        print("The side of equilateral triangle is", self.__length)

    def area(self):
        print("Area is", (1.732 * self.__length * self.__length) / 4)

    def perimeter(self):
        print("Perimeter is", 3 * self.__length)


class Rhombus(Shapes):

    def __init__(self, diagonalp, diagonalq):
        super().__init__()
        self.__diagonal1 = diagonalp
        self.__diagonal2 = diagonalq

    def print_dimension(self):
        print("The diagonals of rhombus are", self.__diagonal1, self.__diagonal2)

    def area(self):
        print("Area is", (self.__diagonal1 * self.__diagonal2) / 2)

    def perimeter(self):
        print("Perimeter is", self.__diagonal1)


class Circle(Shapes):
    def __init__(self, radius):
        super().__init__()
        self.__r = radius

    def print_dimension(self):
        print("The radius of circle is", self.__r)

    def area(self):
        print("Area is", 3.14 * self.__r * self.__r)

    def perimeter(self):
        print("Circumference is", 2 * 3.14 * self.__r)


class Ellipse(Shapes):
    def __init__(self, majoraxis, minoraxis):
        super().__init__()
        self.__max = majoraxis
        self.__min = minoraxis

    def print_dimension(self):
        print("The major axis and minor axis are", self.__max, self.__min)

    def area(self):
        print("Area is", 3.14 * self.__max * self.__min)

    def perimeter(self):
        print("Perimeter is difficult to calculate")


class Cube(Square):
    def __init__(self, side, lengthofside):
        super().__init__(lengthofside)
        self.__sside = side

    def print_dimension(self):
        print("The major axis and minor axis are", self.__sside, self.__sside)

    def area(self):
        print("Area is", 6 * self.__sside * self.__sside)

    def perimeter(self):
        print("Perimeter is", 12 * self.__sside)


class Cylinder(Shapes):
    def __init__(self, baseradius, height):
        super().__init__()
        self.__baser = baseradius
        self.__height = height

    def print_dimension(self):
        print("The radius and height of cylinder are", self.__baser, self.__height)

    def area(self):
        print("Area is", 3.14 * self.__baser * self.__baser * self.__height)

    def perimeter(self):
        print(" Perimeter is", 2 * 3.14 * self.__baser * (self.__baser + self.__height))


class Pentagon(Shapes):
    def __init__(self, base, apothem):
        super().__init__()
        self.__bases = base
        self.__apothem = apothem

    def print_dimension(self):
        print("The base and apothem of pentagon are", self.__bases, self.__apothem)

    def area(self):
        print("Area is", (5 * self.__bases * self.__apothem) / 2)

    def perimeter(self):
        print("Perimeter is", 5 * self.__bases)


x = Rectangle(3, 2)
x.area()
x.perimeter()
x.print_dimension()
print("Color of rectangle x:", x.get_color())
print("Status of rectangle before: ", x.get_fill())
x.set_fill(True)
print("Status of rectangle after: ", x.get_fill())
x.set_color("red")
print("Color of rectangle r1:", x.get_color())

