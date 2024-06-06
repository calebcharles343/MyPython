l = [1, 2, 3, 4, 5]
'''
works on iterables
'''
itr = iter(l)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


def days():
    l = ['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
    i = 0

    while True:
        x = l[i]
        i = (i + 1) % 7
        yield x


d = days()
print(next(d))
print(next(d))
print(next(d))
