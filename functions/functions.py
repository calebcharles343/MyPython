Task = 'How to write a function'
'''
NOTE
Program stages:
1, procedure
2, functions
3, modules
4, application
'''


def add3(a, b, c):
    rtn = a + b + c
    return rtn


r = add3(10, 10, 10)
print(r)


def add(a, b, c):
    print('inside func', id(a), id(b), id(c))


x, y, z = 10, 15, 5

add(x,y,z)
print('outside func', id(x), id(y), id(z))


