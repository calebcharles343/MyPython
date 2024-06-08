# Note decorator function must take outer function as parameter
# and must be called by the nested function
def decorator(fun):
    def wrapper():
        print('*' * 10)
        fun()
        print('*' * 10)

    return wrapper


def display():
    print('Hello')


d = decorator(display)
d()

print('2 #################################')


def decorator2(fun):
    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)

    return wrapper


def display(msg):
    print(msg)


d = decorator2(display)
d('Hello')

print('3 #################################')


def decorator3(fun):
    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)

    return wrapper


@decorator3
def display(msg):
    print(msg)

# d = decorator3(display)
d('Hello')
