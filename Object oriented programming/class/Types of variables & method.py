class Rectangle:
    def __init__(self, length, breadth):
        self.length = length  # instance variables as argument
        self.breadth = breadth  # instance variables as argument
        self.a = 10  # instance variables as declaration

    def area(self):
        self.b = 20  # instance variables as declaration
        return self.length * self.breadth

    def parameter(self):
        self.c = 20  # instance variables as declaration
        return 2 * (self.length + self.breadth)


# Note
'''
if a method is accessing instance variables that method 
automatically becomes instance method 
'''

r1 = Rectangle(10, 5)

r2 = Rectangle(15, 7)
