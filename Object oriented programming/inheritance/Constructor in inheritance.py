class Rectangle:  # Rectangle inherits from object and object from class
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        return 2 * (self.length + self.breadth)

'''
r = Rectangle(10, 5)
print(r.area())
print(r.parameter())
'''

class Cuboid(Rectangle):  # cuboid inherits all the attributes of a Rectangle
    def __init__(self, h, l, b):
        super().__init__(l, b)
        self.height = h
    def volume(self):
        return self.length * self.breadth * self.height


c = Cuboid(3,10,20)
print('volume is', c.volume())