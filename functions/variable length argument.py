'''
variable length arguments
note: write * at thr beginning of placeholder argument to
pack values into a tuple
'''

print('variable length arguments')


def func1(a=0, b=0, *args):
    print(type(args), a, b, args)


func1()
func1(10, 20)
func1(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
func1(10, 'Six', 30.40, True)
'''
unpacking arguments
note: write * at the beginning of iterable list action arguments
to distribut its values
'''
print('unpacking arguments')


def func2(a, b, c):
    print(a, b, c)


l1 = [11, 22, 33]

func2(l1[0], l1[1], l1[2])
func2(*l1)
'''
multiple return values
'''
print('multiple return values')


def func3(a, b, c):
    return a + 1, b + 1, c + 1


x, y, z = func3(10, 20, 30)
print(x, y, z)
