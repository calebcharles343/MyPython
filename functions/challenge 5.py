# Sum of Score Ending with Zero

scores = [200, 456, 300, 100, 234, 678]


def sum(list):
    s = 0
    for i in list:
        if i % 10 == 0:
            s += i
    return s


print(sum(scores))