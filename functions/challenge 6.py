# Invert a dictionary i.e. covert keys to values and values to keys

dict1 = {'a': 200, 'b': 456, 'c': 300, 'd': 100, 'e': 234, 'f': 678}


def invert(d):
    new = {}
    for k, v in d.items():
        new[v] = k
    return new


print(invert(dict1))
