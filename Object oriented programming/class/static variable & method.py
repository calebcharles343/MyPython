class Rectangle:
    count = 0  # class/static: variable & remains the same across all instances

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    def area(self):
        self.b = 20
        return self.length * self.breadth

    def parameter(self):
        self.c = 20
        return 2 * (self.length + self.breadth)

    @classmethod # decorator for readability
    def countRectangle(cls):
        print(cls.count)

    # NOTE
    '''
    countRectangle() automatically becomes a "class method"
    because it is accessing onl a class variable
    '''
r1 = Rectangle(10,5)
print(Rectangle.count)

r2 = Rectangle(15,7)
print(Rectangle.count)

r1.countRectangle()
Rectangle.countRectangle() 