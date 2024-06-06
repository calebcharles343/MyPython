print('fun1 ===========>')
gbl = 10
print('outside', gbl)


def fun1(a, b):
    c = a + b
    print('local', c)
    print('global', gbl)


print('outside', gbl)
fun1(30, 40)

print('fun2 ===========>')


def fun2(g):
    print(g * 2)


fun1(9, 8)
fun2(3)

print('fun3 ===========>')

'''
locals() and global()
'''
a, b, c, d = 11, 22, 33, 44


def fun3(a=15, b=25):
    x, y, z = 1, 2, 3
    print('locals =>',locals())


fun3()

print('globals =>',globals())