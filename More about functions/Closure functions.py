def closure():
    msg = 'Hello'

    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)

    return display


d = closure()
d()


def closure2(msg):
    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)

    return display


d = closure2('Hello')
d()
