# Pascal's Triangle


def pascal(n):
    r = [1]
    for i in range(n):
        print(r)
        tr = [0] + r
        r = r + [0]
        nr = [x + y for x, y in zip(r, tr)]
        r = nr


pascal(6)
'''
  nr = []
        for x, y in zip(r, tr):
            nr.append(x, y)
'''
