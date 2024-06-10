class Cuboid:
    def __init__(self, l, b, h):
        print(id(self))
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth

    def total(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.breadth)

    def volume(self):
        print(id(self))
        return self.length * self.breadth * self.height


c1 = Cuboid(10, 5, 3)
print(id(c1))
c1.volume()

c2 = Cuboid(20, 10, 5)
print(id(c2))
c2.volume()
