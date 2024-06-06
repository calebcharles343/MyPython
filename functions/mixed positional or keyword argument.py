'''
all arguments can be positional or keyword
'''


def add1(a, b, c, d, e, f):
    return print(a + b + c + d + e + f)


add1(1, 2, 3, 4, 5, 6)

'''
arguments before / most be positional only
'''


def add2(a, b, /, c, d, e, f):
    return print(a + b + c + d + e + f)


add2(5, 6, 3, f=9, d=8, e=7)

'''
arguments after * most be keyword only 
'''


def add3(a, b, /, c, d, *, e, f):
    return print(a + b + c + d + e + f)


add3(10, 20, c=30, d=40, e=50, f=60)
