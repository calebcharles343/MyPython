# find maximum of 3 numbers
def max3(n1, n2, n3):
    print(max(n1, n2, n3))


max3(5, 9, 12)

max3(-2, 0, -1)


def max4(a, b, c, d):
    if a > b and a > c and a > d:
        print(a)
    elif b > c and b > d:
        print(b)
    elif c > d:
        print(c)
    else:
        print(d)


max4(0,-2,-3,1)
