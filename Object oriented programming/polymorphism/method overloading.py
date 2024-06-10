class Arith1:
    def sum(self, x, y):
        return x + y


a = Arith1()
print(a.sum(10, 5))
print(a.sum(8.5, 7.6))
print(a.sum('Hello ', 'World'))

print('####==> Overloading')


class Arith2:
    def sum(self, x, y, z=None):
        s = x + y
        if z == None:
            return s
        else:
            return s + z


a = Arith2()
print(a.sum(5, 10, 3))
print(a.sum(5, 10))


