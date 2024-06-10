import math

# Write a Class for Circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        return (2 * math.pi) * self.radius


c1 = Circle(7)
print(c1.area())
print(c1.perimeter())
c2 = Circle(20)
print(c2.area())
print(c2.perimeter())
