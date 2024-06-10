'''
print('#####==>Multi level Inheritance from bottom to top level')

class A:
    def show(self):
        print('A')


class B(A):
    pass


class C(B):
    pass


c = C()
c.show()

print(C.mro())
'''

'''
print('#####==> Multiple Inheritance from left to right ')
class A:
    def show(self):
        print('A')


class B:
    def show(self):
        print('B')

class C(A, B):
    pass

c = C()
c.show()

print(C.mro())

'''

'''
print('#####==> Multiple Inheritance from depth first, left to right ')


class A:
    pass


class B(A):
    pass


class X:
    pass


class Y(X):
    pass


class C(B, Y):
    pass


print(C.mro())
'''

print('#####==> Multiple Inheritance from depth first, left to right, peak')


class P:
    pass


class A(P):
    pass


class B(A):
    pass

 
class X(P):
    pass


class Y(X):
    pass


class C(B, Y):
    pass


print(C.mro())
