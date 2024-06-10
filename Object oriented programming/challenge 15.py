# Method Overriding
import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


r = Rectangle(50, 30)
print(r.area())

c = Circle(10)
print(c.area())
