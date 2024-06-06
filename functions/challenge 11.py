item = [1,2,[3,4,[5,6],7],8]

def flatten(l):
    for i in l:
        if hasattr(i, '__iter__'):
            yield from flatten(i)
        else:
            yield i

f = flatten(item)
print(f)