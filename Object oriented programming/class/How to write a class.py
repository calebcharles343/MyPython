class Cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth

    def total(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.breadth)

    def volume(self):
        return self.length * self.breadth * self.height


cuboin1 = Cuboid(5, 10, 3)
print(cuboin1.volume())

cuboin2 = Cuboid(20, 10, 5)
print(cuboin2.volume())
