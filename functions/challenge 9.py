# variable arguments

def minimum(*val, low_limit=None):
    if low_limit is None:
        return print(min(val))
    else:
        l = [x for x in val if x >= low_limit]
        return print(min(l))


minimum(1, 2, 3, 5, 10, -3)
minimum(1, 2, 3, 5, 10, -3, low_limit=-5)
