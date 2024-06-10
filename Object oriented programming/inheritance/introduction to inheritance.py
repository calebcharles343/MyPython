class Rectangle:  # Rectangle inherits from object and object from class
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        return 2 * (self.length + self.breadth)


class Cuboid(Rectangle):  # cuboid inherits all the attributes of a Rectangle
    def __init__(self, h):
        self.height = h
