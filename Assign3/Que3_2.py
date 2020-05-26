from abc import ABC, abstractmethod

#base  abstract class
class Shapes(ABC):
    def __init__(self):
    	pass
 

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

#encapsulation is done using private and public specifiers
#Derived abstract Classes
class Rectangle(Shapes):
    def __init__(self, length, breadth):

         super().__init__()
         self.length = length    				  #public variable
         self.breadth = breadth
         self.__sides = 4        			           #protected variable
         print("Number of sides:", self.__sides)

    def area(self):
        print("Area is", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter is", 2*(self.length + self.breadth))

class Square(Shapes):
    def __init__(self, lengthofside):

        super().__init__()
        self.lengths = lengthofside
        self.__sides = 4
        print("Number of sides are", self.__sides)

    def area(self):
        print("Area is", self.lengths * self.lengths)

    def perimeter(self):
        print("Perimeter is", 4 * self.lengths)

class Triangle(Shapes):


    def __init__(self, length):
        super().__init__()
        self.length = length
        self.__sides = 3
        print("No of sides are", self.__sides)


    def area(self):
        print("Area is",(1.732*self.length *self.length)/4)

    def perimeter(self):
        print("Perimeter is", 3 * self.length)


class Rhombus(Shapes):


    def __init__(self, diagonalp, diagonalq):
        super().__init__()
        self.diagonal1 = diagonalp
        self.diagonal2 = diagonalq
        self.__sides = 4
        print("No of sides are", self.__sides)


    def area(self):
        print("Area is",(self.diagonal1*self.diagonal2)/2)

    def perimeter(self):
        print("Perimeter is",  self.diagonal1)


class Circle(Shapes):
    def __init__(self, radius):
        super().__init__()
        self.r = radius

    def area(self):
        print("Area is", 3.14*self.r*self.r)

    def perimeter(self):
        print("Circumference is", 2 * 3.14 * self.r)

class Ellipse(Shapes):
    def __init__(self, majoraxis, minoraxis):
        super().__init__()
        self.max = majoraxis
        self.min = minoraxis

    def area(self):
        print("Area is", 3.14 * self.max * self.min)

    def perimeter(self):
        print("Perimeter is difficult to calculate")

class Cube(Square):
    def __init__(self, side, lengthofside):
        super().__init__(lengthofside)
        self.sside = side

    def area(self):
        print("Area is", 6 * self.sside * self.sside)

    def perimeter(self):
        print("Perimeter is", 12 * self.sside)


class Cylinder(Shapes):
    def __init__(self, baseradius, height):
        super().__init__()
        self.baser = baseradius
        self.height = height

    def area(self):
        print("Area is", 3.14 * self.baser * self.baser * self.height)


    def perimeter(self):
        print(" Perimeter is", 2 * 3.14 * self.baser * (self.baser + self.height))

class Pentagon(Shapes):
    def __init__(self, base, apothem):
        super().__init__()
        self.bases = base
        self.apothem = apothem

    def area(self):
        print("Area is", (5 * self.bases * self.apothem)/2)

    def perimeter(self):
        print("Perimeter is", 5 * self.bases)


x = Rectangle(3,2)
x.area()
x.perimeter()


