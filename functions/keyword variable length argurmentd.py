'''
variable length arguments
forms a tuple
'''


def func1(*args):
    print(type(args), args)


'''
keyword variable length arguments
forms a dictionary
'''


def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(name='charles', roll='student', addr = 'delhi')

'''
mixed arguments
'''


def func3(a, b,*args, **kwargs):
    print(a, b,args, kwargs)
func3(10,20,5,6,41,215,20,name='charles',age=30, location='nigeria')