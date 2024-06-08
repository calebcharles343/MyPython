# FUNCTION AS PARAMETER

def display():
    print('hello world')


def fun(d):
    d()


fun(display)


def add(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def exe(func, x, y):
    func(x, y)


exe(add, 15, 10)
exe(sub, 15, 10)


# FUNCTION RETURNING A FUNCTION

def outer():
    def displayInner():
        print('Hello world')

    return displayInner


d = outer()

d()
