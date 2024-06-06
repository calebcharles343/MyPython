def add(a=0, b=0, c=0):
    return print(a + b + c)


add(2, 2)


def add_item(item, l=[]):
    l.append(item)
    return print(l)


l1 = [1, 2, 3, 4, ]
add_item(5, l1)


add_item(22)
add_item(33)
add_item(44)