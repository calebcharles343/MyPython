class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        return 2 * (self.length + self.breadth)

    @staticmethod # for readability
    def isSquare(len, bre):  # Static accesses none of instance or class variables
        return len == bre


ri = Rectangle(10, 5)
print(ri.isSquare(10, 10))
