class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def getlength(self):  # accessor method
        return self.length

    def setlength(self, l):  # mutator method
        self.length = l

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        return 2 * (self.length + self.breadth)

r = Rectangle(10, 5)
print(r.getlength())
print(r.area())
r.setlength(15)
print(r.area())
